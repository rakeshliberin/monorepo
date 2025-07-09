import asyncio
from datetime import datetime
from enum import Enum
import json
import os
import uuid
from livekit import api
from livekit.agents import (
    Agent,
    ChatMessage,
    get_job_context,
    function_tool,
    RunContext,
)
from llama_index.core.schema import MetadataMode

from src.plugins.realtime import RealtimeModel
from src.data import GetBPFromMobileResponse
from src.agents.utils import load_markdown
from src.session_state import SessionState, TTSLanguageCodes
from src.utils import logger

from google.genai import types

RunContext_T = RunContext[SessionState]


class Intent(Enum):
    EMERGENCY = "emergency"
    OUTSTANDING_AMOUNT = "outstanding_amount"
    BILL_UNDERSTANDING = "bill_understanding"
    SERVICE_QUERY = "service_query"
    GENERAL_QUERY = "general_query"
    END_CONVERSATION = "end_conversation"
    UNRELATED_QUERY = "unrelated_query"


class PhoneAgentRealtime(Agent):
    def __init__(self, customer_details: GetBPFromMobileResponse):
        super().__init__(
            instructions=load_markdown("phone_agent_realtime_v5.md").replace(
                "{current_date}",
                datetime.now().strftime("%d %B %Y"),
            ),
            llm=RealtimeModel(
                model="gemini-2.0-flash-live-001",
                modalities=[types.Modality.AUDIO],
                voice="Zephyr",
                language=TTSLanguageCodes.HINDI.value,
                temperature=0.3,
                max_output_tokens=512,
                vertexai=False,
                api_version="v1beta",
                realtime_input_config=types.RealtimeInputConfig(
                    turn_coverage=types.TurnCoverage.TURN_INCLUDES_ALL_INPUT,
                ),
                context_window_compression=types.ContextWindowCompressionConfig(
                    trigger_tokens=25600,
                    sliding_window=types.SlidingWindow(target_tokens=12800),
                ),
            ),
        )

        self._customer_details = customer_details
        self._rag_retriever = get_job_context().proc.userdata["rag_retriever"]

    async def on_enter(self) -> None:
        await self.session.generate_reply(user_input="SESSION_START")

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
    async def end_conversation(self) -> None:
        """
        Use this tool to end the conversation when the user do not need any more help.
        """
        logger.info("---- Ending Conversation ------")

        ctx = get_job_context()
        if ctx is None:
            logger.error("Job context is not found")
            return

        await ctx.api.room.delete_room(api.DeleteRoomRequest(room=ctx.room.name))

    async def transfer_to_emergency(self, ctx: RunContext_T):
        """Transfer the call to a emergency number, Call immediately after request."""

        logger.info("---- Transferring to Emergency ------")

        session_state: SessionState = ctx.userdata
        ctx = session_state.ctx
        room_name = ctx.room.name

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

    async def transfer_to_senior_executive(self) -> dict:
        """Transfer the call to a senior executive. Should be called immediately after user request."""

        logger.info("---- Transferring to Senior Executive ------")

        session_state: SessionState = self.session.userdata
        ctx = session_state.ctx
        room_name = ctx.room.name

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
