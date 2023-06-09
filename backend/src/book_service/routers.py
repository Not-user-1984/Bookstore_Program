from fastapi import APIRouter, Depends
from book_service import models
from book_service.operations import OperationsBooks
from auth.database import get_user_db
from book_service.schemas import BookBase


books_router = APIRouter(
    prefix='/books',
    tags=['books']
)


@books_router.get(
    '/',
    response_model=list[BookBase],
)
def get_operation(
    operations_service: OperationsBooks.get_all_books = Depends(),
):
    return operations_service.get_all_books()
