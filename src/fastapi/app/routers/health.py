from fastapi import APIRouter

router = APIRouter()


@router.get("/", status_code=200)
async def health():
    return {"status": "ok"}
