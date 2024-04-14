from fastapi import APIRouter
from app.services import user_service
from app.models.items import Items

router = APIRouter()


@router.post("/create_user", status_code=201)
async def create_user(item: Items):
    return await user_service.create_user(item)


@router.get("/search_user", status_code=200)
async def search_user(query: str):
    return await user_service.search_user(query)
