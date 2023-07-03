from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud
from db.session import get_async_session
from typing import List
router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate,
                db: Session = Depends(get_async_session)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_async_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/", response_model=List[schemas.User])
def get_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_async_session)
):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int,
    user: schemas.UserUpdate,
    db: Session = Depends(get_async_session)
):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user=user, db_user=db_user)


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_async_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db=db, user=db_user)
    return {"message": "User deleted"}


@router.get("/profile/{user_id}", response_model=schemas.ProfileUser)
def get_profile(user_id: int, db: Session = Depends(get_async_session)):
    db_profile = crud.get_profile(db, user_id=user_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile


@router.put("/profile/{user_id}", response_model=schemas.ProfileUser)
def update_profile(user_id: int, profile: schemas.ProfileUserUpdate, db: Session = Depends(get_async_session)):
    db_profile = crud.get_profile(db, user_id=user_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return crud.update_profile(db=db, profile=profile, db_profile=db_profile)


@router.get("/books/", response_model=List[schemas.Book])
def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_async_session)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@router.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_async_session)):
    return crud.create_book(db=db, book=book)


@router.get("/books/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_async_session)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_async_session)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book(db=db, book=book, db_book=db_book)


@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_async_session)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db=db, book=db_book)
    return {"message": "Book deleted"}
