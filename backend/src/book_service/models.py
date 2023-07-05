from db.base_class import Base, metadata
from sqlalchemy import (Boolean, Column, ForeignKey, Integer, String, Table)
from sqlalchemy.orm import relationship
# from auth.models import User

book_tags = Table(
    "book_tags",
    metadata,
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True)
)

favorite_books = Table(
    "favorite_books",
    metadata,
    Column("profileUser_id", Integer, ForeignKey("profileUser.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
)


class Tag(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("Book", secondary=book_tags, back_populates="tags")


class Book(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    is_available = Column(Boolean(), default=True)
    tags = relationship("Tag", secondary=book_tags, back_populates="books")


class ProfileUser(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    books = relationship("Book", back_populates="owner")
    favorite_books = relationship(
        "Book",
        secondary=favorite_books,
        back_populates="favorited_by",
    )
    carts = relationship("Cart", back_populates="owner")


class CartItem(Base):
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey("cart.id", ondelete="CASCADE"))
    cart = relationship("Cart", back_populates="items")
    book_id = Column(Integer, ForeignKey("book.id", ondelete="CASCADE"))
    book = relationship("Book")
    quantity = Column(Integer, nullable=False, default=1)


class Cart(Base):
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey(ProfileUser.id, ondelete="CASCADE")) 
    owner = relationship("ProfileUser", back_populates="carts")
    total_price = Column(Integer, nullable=False, default=0)
    items = relationship("CartItem", back_populates="cart")
