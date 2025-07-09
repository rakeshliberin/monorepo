import asyncio
import time

from livekit.agents import (
    AgentSession,
    AgentStateChangedEvent,
    UserStateChangedEvent,
    ConversationItemAddedEvent,
)
from livekit.agents.voice.events import AgentState, UserState
from src.utils import logger

IDLE_TIMEOUT = 7.0
HEARTBEAT_TIMEOUT = 15.0


class ListeningHandler:
    def __init__(self, session: AgentSession):
        self.session = session

        now = time.monotonic()
        self.t_agent_state = now
        self.t_user_state = now
        self.t_heartbeat = now

        self.agent_state: AgentState | None = None
        self.user_state: UserState = "listening"

        self.session.on("agent_state_changed")(self._on_agent_state_changed)
        self.session.on("user_state_changed")(self._on_user_state_changed)
        self.session.on("conversation_item_added")(self._on_conversation_item_added)
        self.session.on("close")(self._on_close)

        self.watchdog_task = asyncio.create_task(self._watchdog())

    def _on_agent_state_changed(self, evt: AgentStateChangedEvent):
        self.agent_state, self.t_agent_state = evt.new_state, time.monotonic()
        logger.info(f"Agent state: {self.agent_state}")
        logger.info(f"User state: {self.user_state}")

    def _on_user_state_changed(self, evt: UserStateChangedEvent):
        self.user_state, self.t_user_state = evt.new_state, time.monotonic()

    def _on_conversation_item_added(self, _evt: ConversationItemAddedEvent):
        self.t_heartbeat = time.monotonic()

    def _on_close(self, _evt):
        self._closed = True
        self.watchdog_task.cancel()

    async def _watchdog(self):
        logger.info("Watchdog started")
        self._closed = False

        while not self._closed:
            await asyncio.sleep(1)
            now = time.monotonic()

            # 1️⃣ mutual silence
            if (
                self.agent_state == "listening"
                and self.user_state == "listening"
                and now - max(self.t_agent_state, self.t_user_state) > IDLE_TIMEOUT
            ):
                logger.info("Mutual silence")
                await self._recover()

    async def _recover(self):
        await self.session.generate_reply(user_input="...")
