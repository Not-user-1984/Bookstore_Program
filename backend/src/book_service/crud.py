from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.UserUpdate, db_user: models.User):
    if user.email:
        db_user.email = user.email
    if user.password:
        db_user.hashed_password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()


def get_profile(db: Session, user_id: int):
    return db.query(models.ProfileUser).filter(models.ProfileUser.user_id == user_id).first()


def update_profile(db: Session, profile: schemas.ProfileUserUpdate, db_profile: models.ProfileUser):
    if profile.username:
        db_profile.username = profile.username
    db.commit()
    db.refresh(db_profile)
    return db_profile


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def update_book(db: Session, book: schemas.BookUpdate, db_book: models.Book):
    for field, value in book.dict(exclude_unset=True).items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book: models.Book):
    db.delete(book)
    db.commit()
