from importlib import metadata
import os
from openai import AsyncOpenAI
from dataclasses import dataclass
from typing import Any

import litellm as lite
from litellm.types.utils import StreamingChoices

from livekit.agents import (
    ChatContext,
    FunctionTool,
    APIConnectOptions,
    DEFAULT_API_CONNECT_OPTIONS,
    NotGivenOr,
    NOT_GIVEN,
    APITimeoutError,
    APIStatusError,
    APIConnectionError,
    llm,
)
from livekit.agents.utils import is_given
from livekit.plugins.openai.utils import to_fnc_ctx
from openai import types
from openai.types.chat import ChatCompletionToolChoiceOptionParam

from src.utils import logger
from pydantic import BaseModel
from langfuse import Langfuse
from langfuse.decorators import observe
from typing import Optional


@dataclass
class _LLMOptions:
    model: str
    temperature: NotGivenOr[float]
    max_output_tokens: NotGivenOr[int]
    top_p: NotGivenOr[float]
    top_k: NotGivenOr[float]
    parallel_tool_choice: NotGivenOr[bool]
    tool_choice: NotGivenOr[llm.ToolChoice]


class LLMStream(llm.LLMStream):
    def __init__(
        self,
        llm: llm.LLM,
        *,
        model: str,
        temperature: float,
        top_p: float,
        top_k: float,
        max_output_tokens: int,
        chat_ctx: ChatContext,
        tools: list[FunctionTool],
        conn_options: APIConnectOptions,
        extra_kwargs: dict[str, Any],
        langfuse: Optional[Langfuse] = None,
        trace_id: Optional[str] = None,
        client: AsyncOpenAI = None,
    ) -> None:
        super().__init__(llm, chat_ctx=chat_ctx, tools=tools, conn_options=conn_options)
        self._model = model
        self._llm = llm
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_output_tokens
        self.top_k = top_k
        self._extra_kwargs = extra_kwargs
        self._langfuse = langfuse
        self._trace_id = trace_id
        self._client = client

    async def _run(self) -> None:
        # current function call that we're waiting for full completion (args are streamed)
        # (defined inside the _run method to make sure the state is reset for each run/attempt)
        self._litellm_stream = None
        self._tool_call_id: str | None = None
        self._fnc_name: str | None = None
        self._fnc_raw_arguments: str | None = None
        self._tool_index: int | None = None
        retryable = True

        try:
            chat_ctx, _ = self._chat_ctx.to_provider_format(format="openai")
            fnc_ctx = to_fnc_ctx(self._tools) if self._tools else NOT_GIVEN

            self._litellm_stream = stream = await self._client.chat.completions.create(
                messages=chat_ctx,
                tools=fnc_ctx,
                model=self._model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stream=True,
                reasoning_effort="low",
                stream_options={"include_usage": True},
                metadata={
                    "existing_trace_id": self._langfuse.get_trace_id(),  # set langfuse trace ID
                    "session_id": self._trace_id,
                },
            )

            async for chunk in stream:
                logger.info(f"Chunk: {chunk}")
                for choice in chunk.choices:
                    chat_chunk = self._parse_choice(chunk.id, choice)
                    if chat_chunk is not None:
                        retryable = False
                        self._event_ch.send_nowait(chat_chunk)

                # if chunk.usage is not None:
                #     retryable = False
                #     tokens_details = chunk.usage.prompt_tokens_details
                #     cached_tokens = (
                #         tokens_details.cached_tokens if tokens_details else 0
                #     )
                #     chunk = llm.ChatChunk(
                #         id=chunk.id,
                #         usage=llm.CompletionUsage(
                #             completion_tokens=chunk.usage.completion_tokens,
                #             prompt_tokens=chunk.usage.prompt_tokens,
                #             prompt_cached_tokens=cached_tokens or 0,
                #             total_tokens=chunk.usage.total_tokens,
                #         ),
                #     )
                #     self._event_ch.send_nowait(chunk)

            # for choice in self._response.choices:
            #     chunk = self._parse_choice(self._response.id, choice)
            #     logger.info(f"Response from the model: {chunk}")
            #     if chunk is not None:
            #         retryable = False
            #         self._event_ch.send_nowait(chunk)

            # async for chunk in stream:
            #     for choice in chunk.choices:
            #         chat_chunk = self._parse_choice(chunk.id, choice)
            #         if chat_chunk is not None:
            #             retryable = False
            #             self._event_ch.send_nowait(chat_chunk)

            # if chunk.usage is not None:
            #     retryable = False
            #     tokens_details = chunk.usage.prompt_tokens_details
            #     cached_tokens = (
            #         tokens_details.cached_tokens if tokens_details else 0
            #     )
            #     chunk = llm.ChatChunk(
            #         id=chunk.id,
            #         usage=llm.CompletionUsage(
            #             completion_tokens=chunk.usage.completion_tokens,
            #             prompt_tokens=chunk.usage.prompt_tokens,
            #             prompt_cached_tokens=cached_tokens or 0,
            #             total_tokens=chunk.usage.total_tokens,
            #         ),
            #     )
            #     self._event_ch.send_nowait(chunk)

        except APITimeoutError:
            raise APITimeoutError(retryable=retryable) from None
        except APIStatusError as e:
            raise APIStatusError(
                e.message,
                status_code=e.status_code,
                request_id=e.request_id,
                body=e.body,
                retryable=retryable,
            ) from None
        except Exception as e:
            raise APIConnectionError(retryable=retryable) from e

    def _parse_choice(self, id: str, choice: StreamingChoices) -> llm.ChatChunk | None:
        delta = choice.delta

        # https://github.com/livekit/agents/issues/688
        # the delta can be None when using Azure OpenAI (content filtering)
        if delta is None:
            return None

        if delta.tool_calls:
            for tool in delta.tool_calls:
                if not tool.function:
                    continue

                call_chunk = None
                if self._tool_call_id and tool.id and tool.index != self._tool_index:
                    call_chunk = llm.ChatChunk(
                        id=id,
                        delta=llm.ChoiceDelta(
                            role="assistant",
                            content=delta.content,
                            tool_calls=[
                                llm.FunctionToolCall(
                                    arguments=self._fnc_raw_arguments or "",
                                    name=self._fnc_name or "",
                                    call_id=self._tool_call_id or "",
                                )
                            ],
                        ),
                    )
                    self._tool_call_id = self._fnc_name = self._fnc_raw_arguments = None

                if tool.function.name:
                    self._tool_index = tool.index
                    self._tool_call_id = tool.id
                    self._fnc_name = tool.function.name
                    self._fnc_raw_arguments = tool.function.arguments or ""
                elif tool.function.arguments:
                    self._fnc_raw_arguments += tool.function.arguments  # type: ignore

                if call_chunk is not None:
                    return call_chunk

        if choice.finish_reason in ("tool_calls", "stop") and self._tool_call_id:
            call_chunk = llm.ChatChunk(
                id=id,
                delta=llm.ChoiceDelta(
                    role="assistant",
                    content=delta.content,
                    tool_calls=[
                        llm.FunctionToolCall(
                            arguments=self._fnc_raw_arguments or "",
                            name=self._fnc_name or "",
                            call_id=self._tool_call_id or "",
                        )
                    ],
                ),
            )
            self._tool_call_id = self._fnc_name = self._fnc_raw_arguments = None
            return call_chunk

        return llm.ChatChunk(
            id=id,
            delta=llm.ChoiceDelta(content=delta.content, role="assistant"),
        )


class LiteLLM(llm.LLM):

    def __init__(
        self,
        *,
        model: str = os.getenv("VERTEX_AI_MODEL"),
        temperature: NotGivenOr[float] = NOT_GIVEN,
        top_p: NotGivenOr[float] = NOT_GIVEN,
        top_k: NotGivenOr[float] = NOT_GIVEN,
        max_output_tokens: NotGivenOr[int] = NOT_GIVEN,
        parallel_tool_calls: NotGivenOr[bool] = NOT_GIVEN,
        tool_choice: NotGivenOr[llm.ToolChoice] = NOT_GIVEN,
        langfuse: Optional[Langfuse] = None,
        trace_id: Optional[str] = None,
        client: AsyncOpenAI = None,
    ):
        super().__init__()
        self._opts = _LLMOptions(
            model=model,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            top_p=top_p,
            top_k=top_k,
            tool_choice=tool_choice,
            parallel_tool_choice=parallel_tool_calls,
        )
        self._langfuse = langfuse
        self._trace_id = trace_id
        self._client = client
        lite.success_callback = ["langfuse"]
        lite.failure_callback = ["langfuse"]

    def chat(
        self,
        *,
        chat_ctx: ChatContext,
        tools: list[FunctionTool] | None = None,
        conn_options: APIConnectOptions = DEFAULT_API_CONNECT_OPTIONS,
        parallel_tool_calls: NotGivenOr[bool] = NOT_GIVEN,
        tool_choice: NotGivenOr[llm.ToolChoice] = NOT_GIVEN,
        extra_kwargs: NotGivenOr[dict[str, Any]] = NOT_GIVEN,
    ) -> LLMStream:
        extra = {}
        if is_given(extra_kwargs):
            extra.update(extra_kwargs)

        parallel_tool_calls = (
            parallel_tool_calls
            if is_given(parallel_tool_calls)
            else self._opts.parallel_tool_choice
        )
        if is_given(parallel_tool_calls):
            extra["parallel_tool_calls"] = parallel_tool_calls

        tool_choice = (
            tool_choice if is_given(tool_choice) else self._opts.tool_choice
        )  # type: ignore

        if is_given(tool_choice):
            oai_tool_choice: ChatCompletionToolChoiceOptionParam
            if tool_choice in ("auto", "required", "none"):
                oai_tool_choice = tool_choice
                extra["tool_choice"] = oai_tool_choice

        return LLMStream(
            self,
            model=self._opts.model,
            temperature=self._opts.temperature,
            top_p=self._opts.top_p,
            top_k=self._opts.top_k,
            chat_ctx=chat_ctx,
            tools=tools or [],
            conn_options=conn_options,
            max_output_tokens=self._opts.max_output_tokens,
            langfuse=self._langfuse,
            trace_id=self._trace_id,
            client=self._client,
            extra_kwargs=extra,
        )
