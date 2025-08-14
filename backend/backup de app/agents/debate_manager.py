from __future__ import annotations
import asyncio
import datetime as dt
from typing import List
from .message_bus import MessageBus
from .base_agent import BaseAgent

class DebateManager:
    def __init__(self, bus: MessageBus, agents: List[BaseAgent]) -> None:
        self.bus = bus
        self.agents = agents
        self._tasks: List[asyncio.Task] = []

    async def start(self, initial_prompt: str = "Let's discuss!") -> None:
        await self.bus.publish({
            "sender": "system",
            "content": initial_prompt,
            "timestamp": dt.datetime.utcnow().isoformat(),
        })
        
        for agent in self.agents:
            self._tasks.append(asyncio.create_task(agent.run()))
        
        await asyncio.gather(*self._tasks)

    async def inject_prompt(self, prompt: str) -> None:
        await self.bus.publish({
            "sender": "user",
            "content": prompt,
            "timestamp": dt.datetime.utcnow().isoformat(),
        })
