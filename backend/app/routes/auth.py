from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/login")
async def login():
    return {"message": "Login endpoint"}
