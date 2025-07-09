from enum import Enum
from dataclasses import dataclass
from livekit.agents import JobContext
from llama_index.core.retrievers import BaseRetriever


class TTSLanguageCodes(Enum):
    ENGLISH = "en-IN"
    HINDI = "hi-IN"


@dataclass
class SessionState:
    ctx: JobContext
    tts_language_code: TTSLanguageCodes = TTSLanguageCodes.HINDI
    stt_language_code: str = "hi"
    digit_mode: bool = False
    bill_retriever: BaseRetriever = None
    vertex_credentials: str = ""
    bill_collection: str = ""
