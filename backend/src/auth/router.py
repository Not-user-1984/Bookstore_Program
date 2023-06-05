from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserCreate, UserRead
from fastapi import Depends, APIRouter
from fastapi_users import FastAPIUsers


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserCreate, UserRead),
    prefix="/auth",
    tags=["auth"],
)
curred_user = fastapi_users.current_user()


@router.get("/protected-route")
def protected_route(user: User = Depends(curred_user)):
    return f'Привет, {user.username}'


@router.get("/unprotected-route")
def unprotected_route():
    return 'привет, друг!!'
