import logging

from fastapi import APIRouter
from app.services import scraper_service
from app.models.args import Args

router = APIRouter()


@router.post("/scrap", status_code=200)
async def scraper(args: Args):
    logging.info(args)
    logging.info("POST...")
    return scraper_service.scrap(args)
