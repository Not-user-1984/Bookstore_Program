from db.base_class import Base
from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi_users import FastAPIUsers, models


# Обновляем модель пользователя для использования FastAPI Users
class UserTable(Base, models.BaseUserTable):
    pass


# Обновляем модель пользователя для использования FastAPI Users
class UserCreate(models.BaseUserCreate):
    pass


# Обновляем модель пользователя для использования FastAPI Users
class UserUpdate(models.BaseUserUpdate):
    pass


# Обновляем модель пользователя для использования FastAPI Users
class UserDB(UserTable, models.BaseUserDB):
    pass


# Создаем экземпляр базы данных пользователей
user_db = SQLAlchemyUserDatabase(UserDB, Base)


# Добавляем модели для ролей пользователей
class UserRole(Base):
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey(UserDB.id), nullable=False)
    user = relationship(UserDB, back_populates="roles")


# Добавляем модель токена пользователя
class UserToken(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(UserDB.id), nullable=False)
    user = relationship(UserDB, back_populates="tokens")
    token = Column(String, nullable=False)
    expires_at = Column(Integer, nullable=False)


# Обновляем модель профиля пользователя
class ProfileUser(Base):
    id = Column(Integer, primary_key=True, index=True)
    user = relationship(UserDB, back_populates="owner")
    username = Column(String, unique=True, nullable=False)
    books = relationship("Book", back_populates="owner")
    favorite_books = relationship(
        "Book",
        secondary=favorite_books,
        back_populates="favorited_by",
    )
    carts = relationship("Cart", back_populates="owner")
    roles = relationship(UserRole, back_populates="user")


# Обновляем модель книги
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


# Остальные модели оставляем без изменений

