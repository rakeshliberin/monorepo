from datetime import datetime
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
)
from livekit.agents.stt.stt import SpeechEvent, SpeechEventType
from livekit.rtc.audio_frame import AudioFrame
from livekit.plugins import openai, google

from llama_index.core.retrievers import BaseRetriever
from llama_index.core.schema import MetadataMode
from torch import mode


from src.data.customer_details import GetBPFromMobileResponse
from src.agents.utils import load_markdown
from src.plugins.sarvam_tts import SarvamTTS
from src.session_state import SessionState, TTSLanguageCodes
from src.utils import logger

RunContext_T = RunContext[SessionState]


class PhoneAgentOpenAI(Agent):
    def __init__(self, mobile_details: GetBPFromMobileResponse):
        super().__init__(
            instructions=load_markdown("phone_agent_instructions_v2.txt").format(
                current_date=datetime.now().strftime("%d %B %Y"),
                last_name=mobile_details.last_name,
            ),
            llm=openai.LLM(
                model="gemini-2.5-flash",
                temperature=0.3,
                max_output_tokens=512,
            ),
        )
        self._mobile_details = mobile_details

    async def on_enter(self) -> None:
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

    # async def on_user_turn_completed(
    #     self, turn_ctx: ChatContext, new_message: ChatMessage
    # ) -> None:

    #     job_ctx = get_job_context()

    #     rag_retriever: BaseRetriever = job_ctx.proc.userdata["rag_retriever"]

    #     hits = await rag_retriever.aretrieve(new_message.text_content)

    #     if not hits:
    #         return await super().on_user_turn_completed(turn_ctx, new_message)

    #     # 2. compose context block
    #     context_block = "\n\n---\n".join(
    #         f"[{h.metadata.get('source', 'doc')}] {h.node.get_content(metadata_mode=MetadataMode.LLM)}"
    #         for h in hits
    #     )

    #     # 3. Inject as a *system* message so model treats it as trusted knowledge
    #     turn_ctx.add_message(
    #         role="user",
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

    @function_tool()
    async def get_outstanding_details(self) -> str:
        """
        Get the outstanding details of the customer.
        """
        return self._mobile_details.outstanding_details

    @function_tool()
    async def get_billing_information(self) -> str:
        """
        Get the billing information of the customer.
        """
        return self._mobile_details.billing_information

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

    @function_tool()
    async def end_conversation(self) -> None:
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

    @function_tool()
    async def transfer_to_emergency(self, ctx: RunContext_T):
        """Transfer the call to a emergency number, Call immediately after request."""

        session_state: SessionState = ctx.userdata
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

    @function_tool()
    async def transfer_to_senior_executive(self) -> dict:
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
