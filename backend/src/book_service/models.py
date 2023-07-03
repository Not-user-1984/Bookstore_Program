from db.base_class import Base
from sqlalchemy import (JSON, Boolean, Column, ForeignKey, Integer, String,
                        Table,)
from sqlalchemy.orm import relationship
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi_users import FastAPIUsers, models


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(models.BaseUserUpdate):
    pass


class UserDB(UserTable, models.BaseUserDB):
    pass


user_db = SQLAlchemyUserDatabase(UserDB, Base)


user_roles = Table(
    'user_roles',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('role_name', String),
    Column('user_id', Integer, ForeignKey("user.id")),
    Column("permissions", JSON)
)

book_tags = Table(
    "book_tags",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True)

)

favorite_books = Table(
    "favorite_books",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
)


class UserRole(Base):
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey(UserDB.id), nullable=False)
    user = relationship(UserDB, back_populates="roles")


class UserToken(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(UserDB.id), nullable=False)
    user = relationship(UserDB, back_populates="tokens")
    token = Column(String, nullable=False)
    expires_at = Column(Integer, nullable=False)


class Book(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    is_available = Column(Boolean(), default=True)
    owner_id = Column(Integer, ForeignKey(UserDB.id))
    owner = relationship(UserDB, back_populates="books")
    tags = relationship("Tag", secondary=book_tags, back_populates="books")


class Tag(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("Book", secondary=book_tags, back_populates="tags")


class ProfileUser(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(UserDB.id), nullable=False, unique=True)
    user = relationship(UserDB, back_populates="profile")
    username = Column(String, unique=True, nullable=False)
    books = relationship("Book", back_populates="owner")
    favorite_books = relationship(
        "Book",
        secondary=favorite_books,
        back_populates="favorited_by",
    )
    carts = relationship("Cart", back_populates="owner")
    roles = relationship(UserRole, back_populates="user")


class Cart(Base):
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="carts")
    total_price = Column(Integer, nullable=False, default=0)
    items = relationship("CartItem", back_populates="cart")


class CartItem(Base):
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey("cart.id"))
    cart = relationship("Cart", back_populates="items")
    book_id = Column(Integer, ForeignKey("book.id"))
    book = relationship("Book")
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Integer, nullable=False)
