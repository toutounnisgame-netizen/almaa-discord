from __future__ import annotations
import asyncio
from typing import Dict, Any

class MessageBus:
    def __init__(self) -> None:
        self._queues: Dict[str, asyncio.Queue] = {}
        self._lock = asyncio.Lock()

    async def register(self, subscriber_name: str) -> asyncio.Queue:
        async with self._lock:
            if subscriber_name not in self._queues:
                self._queues[subscriber_name] = asyncio.Queue()
            return self._queues[subscriber_name]

    async def unregister(self, subscriber_name: str) -> None:
        async with self._lock:
            self._queues.pop(subscriber_name, None)

    async def publish(self, message: Dict[str, Any]) -> None:
        queues = list(self._queues.values())
        for q in queues:
            try:
                q.put_nowait(message)
            except asyncio.QueueFull:
                pass
