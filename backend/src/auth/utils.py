from auth.models import User
from db.session import get_async_session
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
        session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
