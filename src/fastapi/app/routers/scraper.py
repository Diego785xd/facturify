from fastapi import APIRouter
from app.services import scraper_service

router = APIRouter()


@router.post("/", status_code=200)
async def scraper():
    return await scraper_service.web_scraper()
