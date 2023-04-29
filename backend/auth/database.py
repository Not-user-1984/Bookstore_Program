from typing import AsyncGenerator

from core.config import settings
from db.base_class import Base
from db.models.books import Book, favorite_books
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker

DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{ settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.PROJECT_NAME }"
Base: DeclarativeMeta = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
        id = Column(Integer, primary_key=True, index=True)
        username = Column(String, nullable=False)
        email: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=False
        )
        hashed_password: Mapped[str] = mapped_column(
            String(length=1024), nullable=False
        )
        is_active: Mapped[bool] = mapped_column(
            Boolean, default=True, nullable=False
            )
        is_superuser: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
        is_verified: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
        books = relationship("Book", back_populates="owner")
        favorite_books = relationship(
            "Book",
            secondary=favorite_books,
            back_populates="favorited_by")
        carts = relationship("Cart", back_populates="owner")


engine = create_async_engine(DATABASE_URL)


async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
    )


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
