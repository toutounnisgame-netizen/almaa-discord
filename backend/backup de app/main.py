from __future__ import annotations
import asyncio
import os
from typing import List, Set
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.agents.message_bus import MessageBus
from app.agents.factory import create_default_agents
from app.agents.debate_manager import DebateManager

app = FastAPI(title="ALMAA Discord IA Backend", version="0.2.0")
router = APIRouter()

bus: MessageBus = None
debate_manager: DebateManager = None
websockets: Set[WebSocket] = set()

class Prompt(BaseModel):
    prompt: str

@router.get("/health")
async def health() -> JSONResponse:
    return JSONResponse({"status": "ok"})

@router.post("/prompt")
async def inject_prompt(prompt: Prompt) -> JSONResponse:
    global debate_manager
    if not debate_manager:
        return JSONResponse({"error": "Not ready"}, status_code=500)
    await debate_manager.inject_prompt(prompt.prompt)
    return JSONResponse({"message": "Prompt injected"})

@app.on_event("startup")
async def startup_event() -> None:
    global bus, debate_manager
    bus = MessageBus()
    agents = create_default_agents(bus=bus)
    debate_manager = DebateManager(bus=bus, agents=agents)
    
    broadcast_queue = await bus.register("broadcast")
    asyncio.create_task(_broadcast_loop(broadcast_queue))
    asyncio.create_task(debate_manager.start("Let's explore AI together!"))

async def _broadcast_loop(queue: asyncio.Queue) -> None:
    while True:
        msg = await queue.get()
        targets = list(websockets)
        for ws in targets:
            try:
                await ws.send_json(msg)
            except Exception:
                websockets.discard(ws)

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket) -> None:
    await ws.accept()
    websockets.add(ws)
    try:
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        pass
    finally:
        websockets.discard(ws)

app.include_router(router, prefix="/api")
