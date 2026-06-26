from fastapi import APIRouter, Request
from ..services.routing import route_request

router = APIRouter()

@router.post("/v1/chat/completions")
async def chat_completions(request: Request):
    payload = await request.json()
    model, prompt = payload.get("model"), payload.get("prompt")
    response = route_request(model, prompt)
    return response
