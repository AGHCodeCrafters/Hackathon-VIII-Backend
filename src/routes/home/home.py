import json
from fastapi import APIRouter

router = APIRouter(tags=["Home"])



@router.get("/")
async def home():
    return {"app": "Magazyn AGH"}
