from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")


@router.get("/status")
async def status() -> dict[str, str]:
    return {"status": "ok"}
