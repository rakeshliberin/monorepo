from dataclasses import dataclass, field
from typing import Dict, Literal, Optional
from enum import Enum
from livekit.agents import JobContext

import yaml


class SessionLanguage(Enum):
    EN = "en"
    HI = "hi"


@dataclass
class Userdata:
    ctx: Optional[JobContext] = None
    session_language: SessionLanguage = SessionLanguage.HI
    is_greeted: bool = False
    user_intent: Optional[
        Literal[
            "unknown",
            "emergency",
            "billing",
            "general_query",
            "unclear",
        ]
    ] = "unknown"
    last_question: Optional[str] = None
    is_verified: bool = False
    is_completed: bool = False

    def session_summary(self) -> str:
        data = {
            "session_language": self.session_language.name,
            "is_greeted": self.is_greeted,
            "user_intent": self.user_intent,
            "last_question": self.last_question,
            "is_verified": self.is_verified,
            "is_completed": self.is_completed,
        }
        return yaml.dump(data)
