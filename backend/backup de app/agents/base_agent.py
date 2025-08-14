from __future__ import annotations
import os
import asyncio
import datetime as dt
from typing import List, Dict, Any, Optional
import httpx
from .message_bus import MessageBus

class BaseAgent:
    def __init__(self, name: str, persona: str, bus: MessageBus, **kwargs) -> None:
        self.name = name
        self.persona = persona
        self.bus = bus
        self._queue: Optional[asyncio.Queue] = None
        self.history: List[Dict[str, Any]] = []

    async def register(self) -> None:
        self._queue = await self.bus.register(self.name)

    async def run(self) -> None:
        if self._queue is None:
            await self.register()
        
        intro = {
            "sender": self.name,
            "content": f"Hello, I am {self.name}. {self.persona}",
            "timestamp": dt.datetime.utcnow().isoformat(),
        }
        await self.bus.publish(intro)
        
        while True:
            message = await self._queue.get()
            if message.get("sender") == self.name:
                continue
                
            response = {
                "sender": self.name,
                "content": f"[{self.name}] Response to: {message.get('content', '')[:50]}...",
                "timestamp": dt.datetime.utcnow().isoformat(),
            }
            await self.bus.publish(response)
            await asyncio.sleep(1)  # Éviter spam
