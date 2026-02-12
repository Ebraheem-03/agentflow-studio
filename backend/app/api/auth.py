from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LoginReq(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginReq):
    # Demo auth stub
    return {"token": "demo-token", "user": {"name": data.username}}

