from auth.models import User
from book_service.models import ProfileUser
from db.session import get_async_session
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
        session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


class ProfileUserManager:
    def __init__(self,
                 db: get_async_session):
        self.db = db

    async def create(self, user: User) -> ProfileUser:
        profile_user = ProfileUser(user=user)
        self.db.add(profile_user)
        self.db.commit()
        self.db.refresh(profile_user)
        return profile_user
