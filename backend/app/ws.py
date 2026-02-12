from fastapi import APIRouter, WebSocket
import asyncio
import json

router = APIRouter()

# Simulates trace events
async def simulate_traces(ws: WebSocket):
    nodes = ["start", "llm_call", "tool_call", "end"]
    for n in nodes:
        await asyncio.sleep(1)
        await ws.send_json({"event": "node_started", "node": n})
        await asyncio.sleep(0.5)
        await ws.send_json({
            "event": "node_finished",
            "node": n,
            "state": {"last_node": n}
        })
    await ws.send_json({"event":"done"})

@router.websocket("/trace/{session}")
async def trace_ws(ws: WebSocket, session: str):
    await ws.accept()
    await simulate_traces(ws)
    await ws.close()

