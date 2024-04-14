from fastapi import APIRouter
from app.services import ocr_service
import requests

router = APIRouter()


@router.post("/ocr", status_code=200)
async def ocr(image_name: str):

    return await ocr_service.process_ocr(image_name)
