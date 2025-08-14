"""
Debate manager orchestrating multi‑agent discussions.

The DebateManager is responsible for initialising agents, triggering
the first topic and running all agent loops concurrently.  It also
allows external components to inject prompts into the conversation.
"""

from __future__ import annotations

import asyncio
import datetime as dt
from typing import List

from .message_bus import MessageBus
from .base_agent import BaseAgent


class DebateManager:
    """Coordinates conversations between a group of agents."""

    def __init__(self, bus: MessageBus, agents: List[BaseAgent]) -> None:
        self.bus = bus
        self.agents = agents
        self._tasks: List[asyncio.Task] = []

    async def start(self, initial_prompt: str = "Let us discuss today's topic.") -> None:
        """
        Publish an initial prompt and launch all agents concurrently.  This
        method does not return until all agent tasks complete (which
        effectively never happens since the agents run infinite loops).
        It should therefore be scheduled as a background task.
        """
        # Broadcast initial message from a synthetic "system" sender
        await self.bus.publish({
            "sender": "system",
            "content": initial_prompt,
            "timestamp": dt.datetime.utcnow().isoformat(),
        })
        # Launch agents concurrently
        for agent in self.agents:
            self._tasks.append(asyncio.create_task(agent.run()))
        # Wait for all tasks
        await asyncio.gather(*self._tasks)

    async def inject_prompt(self, prompt: str) -> None:
        """
        Inject a new user prompt into the conversation.  This can be
        called from an API endpoint to influence the ongoing debate.
        """
        await self.bus.publish({
            "sender": "user",
            "content": prompt,
            "timestamp": dt.datetime.utcnow().isoformat(),
        })