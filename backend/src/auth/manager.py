from typing import Optional
from db.session import get_async_session
from auth.models import User
from auth.utils import get_user_db, ProfileUserManager
from config import Settings
from fastapi import Depends, Request
from fastapi_users import (BaseUserManager, IntegerIDMixin, exceptions, models,
                           schemas)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    # def __init__(self, db: get_async_session):
    #     super().__init__(User, db)
    #     self.profile_user_manager = ProfileUserManager(db)

    reset_password_token_secret = Settings.SECRET_AUTH
    verification_token_secret = Settings.SECRET_AUTH

    async def on_after_register(
            self,
            user: User,
            request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)


        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )

        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        user_dict["role_id"] = 1

        user_dict["profile_user_id"] = 1
        created_user = await self.user_db.create(user_dict)
        profile_user = await ProfileUserManager.create(created_user)
        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
