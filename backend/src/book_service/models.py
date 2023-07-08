from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from db.base import Base

book_tags = Table(
    "book_tags",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True),
    extend_existing=True
)


favorite_books = Table(
    "favorite_books",
    Base.metadata,
    Column(
        "profileUser_id",
        Integer,
        ForeignKey("profileUser.id"),
        primary_key=True
            ),
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
    extend_existing=True
)


class ProfileUser(Base):
    __tablename__ = "profileUser"
    __table_args__ = {'extend_existing': True}

    user = relationship(
        "auth.models.User",
        back_populates="profile_user",
        uselist=False,
        cascade="all, delete"
        )
    books = relationship("Book", back_populates="owner", cascade="all, delete")
    favorite_books = relationship(
        "Book",
        secondary=favorite_books,
        back_populates="favorited_by",
        cascade="all, delete")
    carts = relationship("Cart", back_populates="owner", cascade="all, delete")


class Book(Base):

    __tablename__ = "book"
    __table_args__ = {'extend_existing': True}

    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    category = relationship(
        "Category",
        backref=backref("books", cascade="all, delete"))
    is_available = Column(Boolean(), default=True)
    tags = relationship(
        "Tag", secondary=book_tags,
        back_populates="books",
        cascade="all, delete")
    owner_id = Column(
        Integer,
        ForeignKey("profileUser.id", ondelete="SET NULL")
        )
    owner = relationship("ProfileUser", back_populates="books")
    favorited_by = relationship(
        "ProfileUser",
        secondary=favorite_books,
        back_populates="favorite_books"
        )


class Category(Base):
    __tablename__ = "category"
    __table_args__ = {'extend_existing': True}

    name = Column(String, nullable=False)


class Tag(Base):
    __tablename__ = "tag"
    __table_args__ = {'extend_existing': True}
    name = Column(String, nullable=False)
    books = relationship(
        "Book",
        secondary=book_tags,
        back_populates="tags",
        cascade="all, delete")


class CartItem(Base):
    __tablename__ = "cartItem"
    __table_args__ = {'extend_existing': True}

    cart_id = Column(Integer, ForeignKey("cart.id", ondelete="CASCADE"))
    cart = relationship("Cart", back_populates="items")
    book_id = Column(Integer, ForeignKey("book.id", ondelete="CASCADE"))
    book = relationship("Book")
    quantity = Column(Integer, nullable=False, default=1)


class Cart(Base):
    __tablename__ = "cart"
    __table_args__ = {'extend_existing': True}

    owner_id = Column(
        Integer,
        ForeignKey("profileUser.id", ondelete="CASCADE")
        )
    owner = relationship("ProfileUser", back_populates="carts")
    total_price = Column(Integer, nullable=False, default=0)
    items = relationship(
        "CartItem",
        back_populates="cart",
        cascade="all, delete"
        )
