from fastapi import APIRouter

router = APIRouter()


@router.get("/health", status_code=200)
async def health():
    return {"status": "ok"}
