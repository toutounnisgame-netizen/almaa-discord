"""
Main entrypoint for the FastAPI application powering the ALMAA
Discord IA backend.

This module wires together the message bus, agents, debate manager,
memory store and WebSocket broadcasting.  Upon startup it launches
concurrent tasks for each agent and a broadcast loop that relays
messages to connected WebSocket clients.  Additional REST endpoints
allow injecting user prompts into the ongoing discussion and querying
basic health.
"""

from __future__ import annotations

import asyncio
import os
from typing import List, Set

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .agents.message_bus import MessageBus
from .agents.factory import create_default_agents
from .agents.debate_manager import DebateManager


app = FastAPI(title="ALMAA Discord IA Backend", version="0.2.0")
router = APIRouter()

# Global objects initialised on startup
bus: MessageBus | None = None
debate_manager: DebateManager | None = None
websockets: Set[WebSocket] = set()


class Prompt(BaseModel):
    """Schema for injecting a prompt into the debate."""
    prompt: str


@router.get("/health")
async def health() -> JSONResponse:
    """Health check endpoint."""
    return JSONResponse({"status": "ok"})


@router.post("/prompt")
async def inject_prompt(prompt: Prompt) -> JSONResponse:
    """
    Inject a user prompt into the ongoing conversation.  This endpoint
    can be used to steer the debate from an external client.
    """
    global debate_manager
    if not debate_manager:
        return JSONResponse({"error": "Debate manager not initialised"}, status_code=500)
    await debate_manager.inject_prompt(prompt.prompt)
    return JSONResponse({"message": "Prompt injected"})


@app.on_event("startup")
async def startup_event() -> None:
    """
    Initialise the message bus, agents, debate manager and background
    tasks when the FastAPI application starts.  This includes
    launching the broadcast loop that relays messages to WebSocket
    clients and starting the multi‑agent debate.
    """
    global bus, debate_manager
    bus = MessageBus()
    # Read configuration from environment variables
    model = os.environ.get("OLLAMA_MODEL", "llama3.1:8b")
    ollama_url = os.environ.get("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
    chroma_host = os.environ.get("CHROMA_HOST", "chroma")
    try:
        chroma_port = int(os.environ.get("CHROMA_PORT", "8000"))
    except ValueError:
        chroma_port = 8000
    # Instantiate agents
    agents = create_default_agents(
        bus=bus,
        model=model,
        ollama_base_url=ollama_url,
        chroma_host=chroma_host,
        chroma_port=chroma_port,
    )
    # Create debate manager
    debate_manager = DebateManager(bus=bus, agents=agents)
    # Register a special broadcast queue for WebSocket broadcasting
    broadcast_queue = await bus.register("broadcast")
    # Launch background tasks
    asyncio.create_task(_broadcast_loop(broadcast_queue))
    asyncio.create_task(debate_manager.start("Let's explore a topic together."))


async def _broadcast_loop(queue: asyncio.Queue) -> None:
    """
    Continuously read messages from the message bus and send them to
    all connected WebSocket clients.  This task runs in the
    background for the lifetime of the application.
    """
    while True:
        msg = await queue.get()
        # Copy websockets to avoid mutation during iteration
        targets = list(websockets)
        for ws in targets:
            try:
                await ws.send_json(msg)
            except Exception:
                # Remove broken websockets
                try:
                    websockets.remove(ws)
                except KeyError:
                    pass


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket) -> None:
    """
    WebSocket endpoint for real‑time updates.  Clients connecting
    here will receive every message published on the message bus.  The
    server ignores any data sent from the client.
    """
    await ws.accept()
    websockets.add(ws)
    try:
        while True:
            # Wait for any message from the client to keep the
            # connection open; we don't process client messages yet
            await ws.receive_text()
    except WebSocketDisconnect:
        pass
    finally:
        websockets.discard(ws)


app.include_router(router, prefix="/api")