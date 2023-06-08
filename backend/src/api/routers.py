from fastapi import APIRouter
from auth import user_router
from src.api.endpoints.books import books_router

main_router = APIRouter()

main_router.include_router(
    user_router,
    prefix="/api/v1",
)
main_router.include_router(
    books_router,
    prefix="/api/v1/books/",
)