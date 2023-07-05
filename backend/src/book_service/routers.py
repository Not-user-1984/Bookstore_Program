from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from book_service import crud, schemas
from db.session import get_async_session

router = APIRouter()


@router.post("/tags/", response_model=schemas.Tag)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_async_session)):
    return crud.create_tag(db=db, tag=tag)


@router.get("/tags/", response_model=List[schemas.Tag])
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_async_session)):
    tags = crud.get_tags(db=db, skip=skip, limit=limit)
    return tags


@router.get("/tags/{tag_id}", response_model=schemas.Tag)
def read_tag(tag_id: int, db: Session = Depends(get_async_session)):
    tag = crud.get_tag(db=db, tag_id=tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@router.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_async_session)):
    return crud.create_book(db=db, book=book)


@router.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_async_session)):
    books = crud.get_books(db=db, skip=skip, limit=limit)
    return books


@router.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_async_session)):
    book = crud.get_book(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_async_session)):
    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_async_session)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_async_session)):
    user = crud.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/profileusers/", response_model=schemas.ProfileUser)
def create_profile_user(profile_user: schemas.ProfileUserCreate, db: Session = Depends(get_async_session)):
    return crud.create_profile_user(db=db, profile_user=profile_user)


@router.get("/profileusers/", response_model=List[schemas.ProfileUser])
def read_profile_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_async_session)):
    profile_users = crud.get_profile_users(db=db, skip=skip, limit=limit)
    return profile_users


@router.get("/profileusers/{profile_user_id}", response_model=schemas.ProfileUser)
def read_profile_user(profile_user_id: int, db: Session = Depends(get_async_session)):
    profile_user = crud.get_profile_user(db=db, profile_user_id=profile_user_id)
    if profile_user is None:
        raise HTTPException(status_code=404, detail="Profile User not found")
    return profile_user


@router.post("/carts/", response_model=schemas.Cart)
def create_cart(cart: schemas.CartCreate, db: Session = Depends(get_async_session)):
    return crud.create_cart(db=db, cart=cart)


@router.get("/carts/", response_model=List[schemas.Cart])
def read_carts(skip: int = 0, limit: int = 100, db: Session = Depends(get_async_session)):
    carts = crud.get_carts(db=db, skip=skip, limit=limit)
    return carts


@router.get("/carts/{cart_id}", response_model=schemas.Cart)
def read_cart(cart_id: int, db: Session = Depends(get_async_session)):
    cart = crud.get_cart(db=db, cart_id=cart_id)
    if cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart
