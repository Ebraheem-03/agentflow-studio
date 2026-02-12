from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RunReq(BaseModel):
    graph_id: str
    input: dict

@router.post("/run/")
def run_graph(data: RunReq):
    # Demo graph output
    return {"status": "ok", "graph_id": data.graph_id, "output": {"demo":"result"}}

