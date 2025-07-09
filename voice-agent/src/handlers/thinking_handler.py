from livekit.agents import AgentSession, AgentStateChangedEvent
from typing import Optional
import asyncio

from src.session_state import SessionState, TTSLanguageCodes


class ThinkingHandler:
    def __init__(self, session: AgentSession, delay: float = 15):
        self._session = session
        self._thinking_handle: Optional[asyncio.Task] = None
        self._delay = delay

    def handle(self):
        if self._session:
            self._session.on("agent_state_changed", self._on_agent_state_changed)

    async def _thinking_task(self):
        await asyncio.sleep(self._delay)
        state: SessionState = self._session.userdata
        if state.tts_language_code == TTSLanguageCodes.HINDI:
            await self._session.say(
                "क्षमा करें, इसमें अपेक्षा से अधिक समय लग गया—मुझे पुनः प्रयास करने दीजिए।"
            )
        else:
            await self._session.say(
                "It is taking time to fetch the information. Please wait."
            )

    def _on_agent_state_changed(self, event: AgentStateChangedEvent):
        if event.new_state == "thinking":
            if self._thinking_handle and not self._thinking_handle.done():
                return

            self._thinking_handle = asyncio.create_task(self._thinking_task())

        elif self._thinking_handle:
            self._thinking_handle.cancel()
            self._thinking_handle = None
