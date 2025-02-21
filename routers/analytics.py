from fastapi import APIRouter

router = APIRouter()


@router.get("/analytics")
async def analytics():
    return {"message": "Hello World"}