from fastapi import APIRouter
from app.services import ocr_service

router = APIRouter()


@router.post("/", status_code=200)
async def ocr():
    return await ocr_service.process_ocr()
