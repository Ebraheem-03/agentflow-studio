from fastapi import FastAPI
from .ws import router as ws_router
from .api import graph, auth

app = FastAPI(title="AgentFlow Studio API")
app.include_router(auth.router, prefix="/auth")
app.include_router(graph.router, prefix="/graph")
app.include_router(ws_router, prefix="/ws")

@app.get("/")
def root():
    return {"message": "Backend running (demo)"}

