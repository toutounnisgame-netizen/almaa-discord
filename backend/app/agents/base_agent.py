"""
Definition of the BaseAgent class and supporting types.

Each agent possesses a name, a persona (personality description) and
keeps an internal history of messages it has seen.  When new messages
arrive on the bus, the agent decides whether to respond based on
simple heuristics.  Responses are generated via the local Ollama LLM
through its OpenAI‑compatible API.  Agents also persist messages to
ChromaDB for vector storage.

This implementation is deliberately lightweight; it does not attempt
to model sophisticated behaviour.  It is intended as a starting
point that mirrors the patterns used in the reference ALMAA
repository.
"""

from __future__ import annotations

import os
import asyncio
import datetime as dt
import uuid
from typing import List, Dict, Any, Optional

import httpx
from chromadb import HttpClient
from chromadb.config import Settings

from .message_bus import MessageBus


class BaseAgent:
    """Abstract base class for conversational agents."""

    def __init__(
        self,
        name: str,
        persona: str,
        bus: MessageBus,
        model: str = "llama3.1:8b",
        ollama_base_url: Optional[str] = None,
        chroma_host: Optional[str] = None,
        chroma_port: Optional[int] = None,
    ) -> None:
        self.name = name
        self.persona = persona
        self.model = model
        self.bus = bus
        self._queue: Optional[asyncio.Queue] = None
        self.history: List[Dict[str, Any]] = []  # chat history for LLM context
        self.ollama_base_url = ollama_base_url or os.environ.get("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
        # Set up ChromaDB client if available
        self.chroma_client: Optional[HttpClient] = None
        self.collection = None
        if chroma_host:
            try:
                self.chroma_client = HttpClient(
                    host=chroma_host,
                    port=chroma_port or 8000,
                )
                # Create or get collection for this agent
                cname = f"conv_{self.name.lower()}"
                try:
                    self.collection = self.chroma_client.get_collection(cname)
                except Exception:
                    self.collection = self.chroma_client.create_collection(name=cname)
            except Exception:
                # Chroma may not be reachable; silently ignore and run without persistence
                self.chroma_client = None
                self.collection = None

    async def register(self) -> None:
        """Register the agent on the message bus."""
        self._queue = await self.bus.register(self.name)

    async def run(self) -> None:
        """
        Main loop of the agent.  Waits for new messages, decides whether
        to respond and publishes responses.  Runs indefinitely until the
        program is cancelled.
        """
        if self._queue is None:
            await self.register()
        # Publish an introductory message announcing the agent's presence
        intro = {
            "sender": self.name,
            "content": f"Hello, I am {self.name}. {self.persona}",
            "timestamp": dt.datetime.utcnow().isoformat(),
        }
        await self.bus.publish(intro)
        self.history.append({"role": "assistant", "content": intro["content"]})
        await self._persist_message(intro)
        # Consume messages forever
        while True:
            message = await self._queue.get()
            # Ignore messages from self
            if message.get("sender") == self.name:
                continue
            content = message.get("content", "")
            # Append to history
            self.history.append({"role": "user", "content": content})
            await self._persist_message(message)
            # Decide whether to respond; simple probability or always respond
            # Here we respond to every message not sent by us
            try:
                response_text = await self._generate_response()
            except Exception as exc:
                response_text = f"[Error generating response: {exc}]"
            response = {
                "sender": self.name,
                "content": response_text,
                "timestamp": dt.datetime.utcnow().isoformat(),
            }
            await self.bus.publish(response)
            self.history.append({"role": "assistant", "content": response_text})
            await self._persist_message(response)

    async def _generate_response(self) -> str:
        """
        Generate a response using the local Ollama server.  Uses the
        OpenAI‑compatible chat completions endpoint.  The prompt is
        constructed from the agent's persona and recent conversation
        history.
        """
        # Limit the context to the last 6 turns to stay within prompt limits
        context = self.history[-6:]
        # Prepend system message describing persona
        messages = [
            {"role": "system", "content": f"You are {self.name}, {self.persona}. Respond concisely."}
        ] + context
        url = f"{self.ollama_base_url.rstrip('/')}/v1/chat/completions"
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "stream": False,
        }
        headers = {
            "Content-Type": "application/json",
            # Ollama requires an API key, but it can be any string when using local models
            "Authorization": "Bearer ollama",
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            res = await client.post(url, json=payload, headers=headers)
            res.raise_for_status()
            data = res.json()
            return data.get("choices")[0]["message"]["content"].strip()

    async def _persist_message(self, msg: Dict[str, Any]) -> None:
        """
        Persist the message to the agent's ChromaDB collection if available.
        Stores the message content as a document with simple metadata.
        """
        if not self.collection:
            return
        try:
            _id = str(uuid.uuid4())
            self.collection.add(
                ids=[_id],
                documents=[msg.get("content", "")],
                metadatas=[{"sender": msg.get("sender"), "timestamp": msg.get("timestamp")}],
            )
        except Exception:
            pass