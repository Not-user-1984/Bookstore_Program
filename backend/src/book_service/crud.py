from sqlalchemy.orm import Session
from book_service import models, schemas


def create_tag(
        db: Session,
        tag: schemas.TagCreate
        ):
    db_tag = models.Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tag).offset(skip).limit(limit).all()


def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        name=book.name,
        author=book.author,
        description=book.description,
        price=book.price,
        category=book.category,
        is_available=book.is_available,

    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        password=user.password,
        full_name=user.full_name,
        is_active=user.is_active,
        is_superuser=user.is_superuser
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_profile_user(db: Session, profile_user: schemas.ProfileUserCreate):
    db_profile_user = models.ProfileUser(
        user_id=profile_user.user_id,
        username=profile_user.username
    )
    db.add(db_profile_user)
    db.commit()
    db.refresh(db_profile_user)
    return db_profile_user


def get_profile_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProfileUser).offset(skip).limit(limit).all()


def get_profile_user(db: Session, profile_user_id: int):
    return db.query(models.ProfileUser).filter(models.ProfileUser.id == profile_user_id).first()


def create_cart(db: Session, cart: schemas.CartCreate):
    db_cart = models.Cart(
        owner_id=cart.owner_id
    )
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart


def get_carts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cart).offset(skip).limit(limit).all()


def get_cart(db: Session, cart_id: int):
    return db.query(models.Cart).filter(models.Cart.id == cart_id).first()
