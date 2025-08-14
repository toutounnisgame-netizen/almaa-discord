"""
Message bus for inter‑agent communication.

The MessageBus maintains an asynchronous queue for each registered
subscriber.  When a message is published, it is dispatched to all
registered queues without blocking.  Agents call `register()` to
obtain their private queue.  Other components (e.g. WebSocket
broadcast) can also register to receive all messages.
"""

from __future__ import annotations

import asyncio
from typing import Dict, Any


class MessageBus:
    """Asynchronous broadcast message bus."""

    def __init__(self) -> None:
        # Mapping of subscriber identifier to its queue
        self._queues: Dict[str, asyncio.Queue] = {}
        # Lock to protect queue registration
        self._lock = asyncio.Lock()

    async def register(self, subscriber_name: str) -> asyncio.Queue:
        """
        Register a subscriber and return an asyncio.Queue from which
        messages can be consumed.  If the subscriber already exists its
        existing queue is returned.
        """
        async with self._lock:
            if subscriber_name not in self._queues:
                self._queues[subscriber_name] = asyncio.Queue()
            return self._queues[subscriber_name]

    async def unregister(self, subscriber_name: str) -> None:
        """Remove a subscriber and discard its queue."""
        async with self._lock:
            self._queues.pop(subscriber_name, None)

    async def publish(self, message: Dict[str, Any]) -> None:
        """
        Broadcast a message to all subscribers.  Uses put_nowait to
        avoid blocking if an agent is temporarily slow to consume.
        """
        # Clone the queues to avoid race conditions while iterating
        queues = list(self._queues.values())
        for q in queues:
            try:
                q.put_nowait(message)
            except asyncio.QueueFull:
                # Drop the message for this subscriber if its queue is full
                pass