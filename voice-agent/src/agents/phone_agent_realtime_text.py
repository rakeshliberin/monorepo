from collections.abc import AsyncGenerator, Coroutine
from datetime import datetime
from enum import Enum
import os
from typing import AsyncIterable
import uuid
from livekit import api
from livekit.agents import (
    Agent,
    ChatContext,
    ChatMessage,
    get_job_context,
    ModelSettings,
    function_tool,
    RunContext,
    llm,
)
from livekit.agents.stt.stt import SpeechEvent, SpeechEventType
from livekit.rtc.audio_frame import AudioFrame
from llama_index.core.retrievers import BaseRetriever
from llama_index.core.schema import MetadataMode

from src.data.customer_details import GetBPFromMobileResponse
from src.agents.utils import load_markdown
from src.plugins.sarvam_tts import SarvamTTS
from src.session_state import SessionState, TTSLanguageCodes
from src.utils import logger, bus

from google.genai import Client, types
from google.genai.live import AsyncSession
from livekit.plugins.google.utils import to_fnc_ctx


RunContext_T = RunContext[SessionState]


class Intent(Enum):
    EMERGENCY = "emergency"
    OUTSTANDING_AMOUNT = "outstanding_amount"
    BILL_UNDERSTANDING = "bill_understanding"
    SERVICE_QUERY = "service_query"
    GENERAL_QUERY = "general_query"
    END_CONVERSATION = "end_conversation"
    UNRELATED_QUERY = "unrelated_query"


class PhoneAgentRealtimeText(Agent):
    def __init__(self, customer_details: GetBPFromMobileResponse):
        super().__init__(
            instructions=load_markdown("phone_agent_realtime_v3.md").format(
                current_date=datetime.now().strftime("%d %B %Y"),
            )
        )
        self._customer_details = customer_details
        self._live_session: AsyncSession | None = None
        self._session_cm = None
        self._client = Client()

        self._rag_retriever: BaseRetriever | None = None

        bus.on("transfer_to_senior_executive", self.transfer_to_senior_executive)
        bus.on("end_conversation", self.end_conversation)
        bus.on("transfer_to_emergency", self.transfer_to_emergency)

    async def on_enter(self) -> None:
        tools = to_fnc_ctx([self.handle_intent])

        self.config = types.LiveConnectConfig(
            system_instruction=load_markdown("phone_agent_realtime_v3.md").format(
                current_date=datetime.now().strftime("%d %B %Y"),
            ),
            temperature=0.3,
            max_output_tokens=512,
            response_modalities=[types.Modality.AUDIO],
            tools=[{"function_declarations": tools}],
        )

        self._session_cm = self._client.aio.live.connect(
            model="gemini-2.0-flash-live-001",
            config=self.config,
        )
        self._live_session = await self._session_cm.__aenter__()

        # Greet immediately, then let the LLM take over.
        # await self.greet_user()
        # # # Listen for user input
        # await self.session.interrupt()  # Stop any current agent speech
        # self.session.clear_user_turn()  # Clear any previous input
        # self.session.input.set_audio_enabled(True)  # Start listening
        if self._mobile_details.status == "error":
            await self.session.say(
                "यह कॉल पंजीकृत मोबाइल नंबर से नहीं है. कृपया पंजीकृत मोबाइल नंबर से कॉल करें।",
                allow_interruptions=False,
            )
            await self.end_conversation()

        await self.session.generate_reply(user_input="SESSION_START")

    # async def greet_user(self) -> None:
    #     """Speak the first line so the user knows we're alive."""
    #     await self.session.generate_reply()

    async def on_exit(self) -> None:
        if self._session_cm:
            await self._session_cm.__aexit__(None, None, None)

    # async def on_user_turn_completed(
    #     self, turn_ctx: ChatContext, new_message: ChatMessage
    # ) -> None:

    #     logger.info("---- On User Turn Completed ------")

    #     if self._rag_retriever is None:
    #         job_ctx = get_job_context()
    #         self._rag_retriever = job_ctx.proc.userdata["rag_retriever"]

    #     hits = await self._rag_retriever.aretrieve(new_message.text_content)

    #     if not hits:
    #         return await super().on_user_turn_completed(turn_ctx, new_message)

    #     # 2. compose context block
    #     context_block = "\n\n---\n".join(
    #         f"[{h.metadata.get('source', 'doc')}] {h.node.get_content(metadata_mode=MetadataMode.LLM)}"
    #         for h in hits
    #     )

    #     # 3. Inject as a *system* message so model treats it as trusted knowledge
    #     turn_ctx.add_message(
    #         role="assistant",
    #         content=[
    #             "<<KNOWLEDGE>>\n",
    #             f"{context_block}",
    #             "<<END_KNOWLEDGE>>\n",
    #         ],
    #     )

    #     ctx = turn_ctx.copy()
    #     ctx.truncate(max_items=500)

    #     await self.update_chat_ctx(ctx)

    #     return await super().on_user_turn_completed(turn_ctx, new_message)

    async def stt_node(
        self, audio: AsyncIterable[AudioFrame], model_settings: ModelSettings
    ) -> AsyncIterable[SpeechEvent | str]:

        async for event in Agent.default.stt_node(self, audio, model_settings):
            if event.type == SpeechEventType.FINAL_TRANSCRIPT:
                logger.info("STT event: %s", event.alternatives[0].text)
                yield event

    async def llm_node(
        self,
        chat_ctx: llm.ChatContext,
        tools: list[llm.FunctionTool],
        model_settings: ModelSettings,
    ) -> AsyncIterable[llm.ChatChunk | str]:
        logger.info("---- LLM Node ------")

        async def generate() -> AsyncIterable[str]:
            turns, _ = chat_ctx.to_provider_format(format="google")
            turns = [types.Content.model_validate(turn) for turn in turns]
            await self._live_session.send_client_content(
                turns=turns, turn_complete=True
            )

            async for msg in self._live_session.receive():
                logger.info(f"Received message: {msg}")
                if msg.server_content:
                    if msg.text is not None:
                        yield msg.text
                elif msg.tool_call:
                    function_responses = []
                    logger.info(f"Received tool call: {msg.tool_call}")
                    for fc in msg.tool_call.function_calls:
                        if fc.name == "handle_intent":
                            intent = fc.args["intent"]
                            query = fc.args["query"]
                            response = await self.handle_intent(intent, query)
                            function_response = types.FunctionResponse(
                                id=fc.id,
                                name=fc.name,
                                response=response,
                            )
                            function_responses.append(function_response)

                    await self._live_session.send_tool_response(
                        function_responses=function_responses
                    )

        return generate()

    @function_tool()
    async def handle_intent(self, intent: str, query: str) -> dict:
        """
        Handle the user's intent. Call this tool when you have detected the user's intent.

        The intent can be one of the following:
        - service_query
        - general_query
        - outstanding_amount
        - bill_understanding
        - emergency
        - unrelated_query
        - end_conversation

        The tool returns the response to the user's intent. This response should be used to answer the user's question.

        Args:
            intent (str): The intent of the user.
            query (str): The query to search the knowledge base for. This is generated from the user's query.
            If the intent is service query, the query should be the ticket type.
            The query should be in english.
            For example, if the user's query is "What is the outstanding amount?", the query will be "outstanding amount".

        Returns:
            dict: The response to the user's intent.
            - result: The response to the user's intent. Use this to answer the user's question.
            - status: The status of the response.
                - success: The response is successful.
                - error: The response is not successful.

        """
        logger.info(f"---- Handling Intent: {intent} | {query} ------")

        if (Intent.SERVICE_QUERY.value in intent.lower()) or (
            Intent.GENERAL_QUERY.value in intent.lower()
        ):
            query = f"ticket type: {query}"
            response = await self.query_knowledgebase(query)
            return {
                "output": response,
                "result": "ok",
            }
        elif Intent.OUTSTANDING_AMOUNT.value in intent.lower():
            return {
                "output": f"{self._customer_details.outstanding_details}",
                "result": "ok",
            }
        elif Intent.BILL_UNDERSTANDING.value in intent.lower():
            return {
                "output": f"{self._customer_details.billing_information} ",
                "result": "ok",
            }
        elif Intent.END_CONVERSATION.value in intent.lower():
            await self.end_conversation()
            return {
                "output": "End the conversation",
                "result": "ok",
            }

        return {
            "error": "I'm sorry, I couldn't handle the user's intent. Please try again.",
            "result": "error",
        }

    async def query_knowledgebase(self, query: str) -> str:
        """
        Query the knowledge base for the given query.

        Args:
            query (str): The query to search the knowledge base for.

        Returns:
            str: The context block of the hits.
        """

        if self._rag_retriever is None:
            job_ctx = get_job_context()
            self._rag_retriever = job_ctx.proc.userdata["rag_retriever"]

        hits = await self._rag_retriever.aretrieve(query)

        if not hits:
            return ""

        # 2. compose context block
        context_block = "\n\n---\n".join(
            f"[{h.metadata.get('source', 'doc')}] {h.node.get_content(metadata_mode=MetadataMode.LLM)}"
            for h in hits
        )

        logger.info(f"Context block: {context_block}")

        return context_block

    @function_tool()
    async def set_session_language(
        self,
        context: RunContext_T,
        language_code: str,
    ) -> str:
        """
        Set the session language. Call this function to set the language of the session.
        This will also update the TTS language code for the session.
        The language code can be either "en-IN" for English or "hi-IN" for Hindi.

        Args:
            language_code(str): The language code to set the session to can be only one of "en-IN" or "hi-IN"
        """
        context.userdata.tts_language_code = TTSLanguageCodes(value=language_code)
        tts: SarvamTTS = context.session.tts
        tts.update_options(language=language_code)
        return language_code

    async def end_conversation(self, *args, **kwargs) -> None:
        """
        Call to end the conversation when the user do not need any more help.
        """
        ctx = get_job_context()
        if ctx is None:
            logger.error("Job context is not found")
            return

        session_state: SessionState = self.session.userdata

        if session_state.tts_language_code == TTSLanguageCodes.HINDI:
            await self.session.say(
                "इंद्रप्रस्थ गैस लिमिटेड में कॉल करने के लिए धन्यवाद। आपका दिन शुभ हो।"
            )
        else:
            await self.session.say(
                "Thank you for calling Indraprastha Gas Limited. Have a great day!"
            )

        await ctx.api.room.delete_room(api.DeleteRoomRequest(room=ctx.room.name))

    async def transfer_to_emergency(self):
        """Transfer the call to a emergency number, Call immediately after request."""

        session_state: SessionState = self.session.userdata
        ctx = session_state.ctx
        room_name = ctx.room.name

        # await self.session.say(
        #     f"I'm transferring you to a human agent now. Please hold while we connect you."
        # )

        logger.info("---- Calling Senior Executive ------")

        # Generate a unique identity for the SIP participant
        identity = f"transfer_{uuid.uuid4().hex[:8]}"

        # Create LiveKit API client
        livekit_url = os.environ.get("LIVEKIT_URL")
        livekit_api_key = os.environ.get("LIVEKIT_API_KEY")
        livekit_api_secret = os.environ.get("LIVEKIT_API_SECRET")
        sip_trunk_id = os.environ.get("LIVEKIT_TRUNK_ID")

        transfer_to = os.environ.get("SENIOR_EXEC_NUMBER", "+919999851423")

        try:
            if ctx and hasattr(ctx, "api"):
                response = await ctx.api.sip.create_sip_participant(
                    api.CreateSIPParticipantRequest(
                        sip_trunk_id=sip_trunk_id,
                        sip_call_to=transfer_to,
                        room_name=room_name,
                        participant_identity=identity,
                        participant_name="Human Agent",
                        krisp_enabled=False,
                        play_dialtone=False,
                        play_ringtone=False,
                    )
                )
            else:
                # Fallback to creating our own API client
                livekit_api = api.LiveKitAPI(
                    url=livekit_url,
                    api_key=livekit_api_key,
                    api_secret=livekit_api_secret,
                )

                response = await livekit_api.sip.create_sip_participant(
                    api.CreateSIPParticipantRequest(
                        sip_trunk_id=sip_trunk_id,
                        sip_call_to=transfer_to,
                        room_name=room_name,
                        participant_identity=identity,
                        participant_name="Human Agent",
                        krisp_enabled=False,
                    )
                )

                await livekit_api.aclose()

            return {
                "phone_number": transfer_to,
                "identity": identity,
                "status": "success",
                "message": "I'm transferring you to a emergency center. Please hold while we connect you.",
            }

        except Exception as e:
            print(f"Error transferring call: {e}")
            await self.session.say(
                f"I'm sorry, I couldn't transfer the call at this time."
            )
            return {
                "phone_number": None,
                "identity": None,
                "status": "error",
                "message": "I'm sorry, I couldn't transfer the call at this time.",
            }

    async def transfer_to_senior_executive(self, *args, **kwargs) -> dict:
        """Transfer the call to a senior executive. Should be called immediately after user request."""

        session_state: SessionState = self.session.userdata
        ctx = session_state.ctx
        room_name = ctx.room.name

        # await self.session.say(
        #     f"I'm transferring you to a human agent now. Please hold while we connect you."
        # )

        logger.info("---- Calling Senior Executive ------")

        # Generate a unique identity for the SIP participant
        identity = f"transfer_{uuid.uuid4().hex[:8]}"

        # Create LiveKit API client
        livekit_url = os.environ.get("LIVEKIT_URL")
        livekit_api_key = os.environ.get("LIVEKIT_API_KEY")
        livekit_api_secret = os.environ.get("LIVEKIT_API_SECRET")
        sip_trunk_id = os.environ.get("LIVEKIT_TRUNK_ID")

        transfer_to = os.environ.get("SENIOR_EXEC_NUMBER", "+919999851423")

        try:
            if ctx and hasattr(ctx, "api"):
                response = await ctx.api.sip.create_sip_participant(
                    api.CreateSIPParticipantRequest(
                        sip_trunk_id=sip_trunk_id,
                        sip_call_to=transfer_to,
                        room_name=room_name,
                        participant_identity=identity,
                        participant_name="Human Agent",
                        krisp_enabled=False,
                        play_dialtone=False,
                        play_ringtone=False,
                    )
                )
            else:
                # Fallback to creating our own API client
                livekit_api = api.LiveKitAPI(
                    url=livekit_url,
                    api_key=livekit_api_key,
                    api_secret=livekit_api_secret,
                )

                response = await livekit_api.sip.create_sip_participant(
                    api.CreateSIPParticipantRequest(
                        sip_trunk_id=sip_trunk_id,
                        sip_call_to=transfer_to,
                        room_name=room_name,
                        participant_identity=identity,
                        participant_name="Human Agent",
                        krisp_enabled=False,
                    )
                )

                await livekit_api.aclose()

            return {
                "phone_number": transfer_to,
                "identity": identity,
                "status": "success",
                "message": "I'm transferring you to a senior executive now. Please hold while we connect you.",
            }

        except Exception as e:
            print(f"Error transferring call: {e}")
            await self.session.say(
                f"I'm sorry, I couldn't transfer the call at this time."
            )
            return {
                "phone_number": None,
                "identity": None,
                "status": "error",
                "message": "I'm sorry, I couldn't transfer the call at this time.",
            }
