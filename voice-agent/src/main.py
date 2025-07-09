import asyncio
import os
from openai import AsyncOpenAI

from datetime import datetime
from typing import AsyncIterable
import uvloop
from dotenv import load_dotenv
from livekit import api, rtc
from livekit.agents import (
    AgentSession,
    JobContext,
    JobProcess,
    RoomInputOptions,
    WorkerOptions,
    cli,
    llm,
    stt,
)
from livekit.plugins import silero, noise_cancellation, sarvam, google
from livekit import api


from src.data import get_bp_from_mobile
from src.agents import PhoneAgentGemini
from src.plugins import SarvamTTS, LiteLLM, deepgram
from src.utils.logger import logger
from src.session_state import SessionState
from src.handlers import ListeningHandler

from langfuse import Langfuse

load_dotenv(override=True)


# --------------------------------------------------------------------------- #
#                                ENTRYPOINT                                   #
# --------------------------------------------------------------------------- #


async def entrypoint(ctx: JobContext):
    logger.info("Starting entrypoint")

    # service_account_file = ""
    # with open("service-account-key.json", "r") as f:
    #     service_account_file = f.read()

    await ctx.connect()

    participants = await ctx.wait_for_participant()

    if participants.kind == rtc.ParticipantKind.PARTICIPANT_KIND_SIP:
        caller_id = participants.attributes["sip.phoneNumber"]
        logger.info(f"Caller ID: {caller_id}")
        details = await get_bp_from_mobile(caller_id)
        logger.info(f"Details: {details}")
    else:
        caller_id = "+919999851423"
        details = await get_bp_from_mobile(caller_id)
        # details = GetBPFromMobileResponse(
        #     status="error",
        #     message="Call not placed from registered valid mobile number.",
        #     outstanding_details="",
        #     billing_information="",
        # )

    logger.info("Connected to the room")

    langfuse: Langfuse = ctx.proc.userdata["langfuse"]

    track_id = f"track_{caller_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    req = api.RoomCompositeEgressRequest(
        room_name=ctx.room.name,
        audio_only=True,
        file_outputs=[
            api.EncodedFileOutput(
                file_type=api.EncodedFileType.OGG,
                disable_manifest=True,
                filepath=f"recordings/{track_id}.ogg",
                # gcp=api.GCPUpload(
                #     credentials=service_account_file,
                #     bucket="igl-voice-agent",
                # ),
            )
        ],
    )

    egress_info = await api.LiveKitAPI().egress.start_room_composite_egress(req)
    # logger.info(f"Egress info: {egress_info}")

    session_state = SessionState(ctx=ctx)

    openai_client = AsyncOpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_API_BASE"),
    )

    session = AgentSession[SessionState](
        userdata=session_state,
        turn_detection="vad",
        vad=ctx.proc.userdata["vad"],
        stt=sarvam.STT(
            api_key=os.environ.get("SARVAM_API_KEY"),
            language="en-IN",
        ),
        llm=LiteLLM(
            model=os.getenv("LITELLM_MODEL"),
            temperature=0.3,
            top_p=0.8,
            top_k=20,
            max_output_tokens=512,
            tool_choice="auto",
            langfuse=langfuse,
            trace_id=track_id,
            client=openai_client,
        ),
        tts=sarvam.TTS(
            api_key=os.environ.get("SARVAM_API_KEY"),
            target_language_code=session_state.tts_language_code.value,
            speaker="anushka",
            enable_preprocessing=True,
        ),
    )

    # session = AgentSession[SessionState](
    #     userdata=session_state,
    # )

    # async def write_transcript():
    #     storage_client = storage.Client()
    #     bucket = storage_client.bucket("igl-voice-agent")
    #     blob = bucket.blob(f"transcription/{track_id}.json")
    #     blob.upload_from_string(
    #         json.dumps(
    #             session.history.to_dict(exclude_timestamp=False),
    #             indent=2,
    #             ensure_ascii=False,
    #         ),
    #         content_type="text/plain; charset=utf-8",
    #     )

    #     logger.info(f"Transcription uploaded to {blob.public_url}")

    # ctx.add_shutdown_callback(lambda _: instrumentation.stop())
    # ctx.add_shutdown_callback(write_transcript)

    await session.start(
        agent=PhoneAgentGemini(details),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC()
        ),
    )

    # thinking_handler = ThinkingHandler(session)
    # thinking_handler.handle()

    ListeningHandler(session)
    # listening_handler.handle(
    #     on_timeout=end_call(ctx),
    # )

    # await api.LiveKitAPI().aclose()


class DummyLLM(llm.LLM):
    async def chat(self, *args, **kwargs):
        raise NotImplementedError("DummyLLM does not support chat")


async def end_call(ctx: JobContext):
    await ctx.api.room.delete_room(api.DeleteRoomRequest(room=ctx.room.name))

    # await lkapi.aclose()


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load(min_speech_duration=0.01)
    proc.userdata["langfuse"] = Langfuse()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    cli.run_app(
        opts=WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=prewarm,
            initialize_process_timeout=60.0,
            job_memory_warn_mb=2048,
        )
    )
