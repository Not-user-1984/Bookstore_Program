from fastapi import APIRouter
from auth import user_router

main_router = APIRouter()

main_router.include_router(
    user_router,
    prefix="/api/v1",
)
