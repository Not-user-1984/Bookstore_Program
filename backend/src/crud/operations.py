from src.db.session import get_session
from src.models import Book
from fastapi import Depends
from sqlalchemy.orm import Session


class OperationsBooks:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all_books(self):
        return self.session.query(Book).all

    def create_books(
            self,
            session: Session,
            name: str,
            author: str,
            description: str,
            price: int,
            category: str,
            owner_id: int):
        new_book = Book(
            name=name,
            author=author,
            description=description,
            price=price,
            category=category,
            owner_id=owner_id
            )
        self.session.add(new_book)
        session.commit()
        session.refresh(new_book)
        return new_book
