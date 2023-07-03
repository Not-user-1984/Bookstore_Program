from auth.utils import get_user_db
from book_service.models import User
from fastapi import Depends
from fastapi_users import (BaseUserManager, IntegerIDMixin, exceptions, models,
                           schemas)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    pass


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
