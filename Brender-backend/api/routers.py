from fastapi import APIRouter

api_v1 = APIRouter(
    prefix="/api/v1",
)


@api_v1.get("/", tags=["Root"])
async def v1_root():
    return {"detail": "Brender API v1"}
