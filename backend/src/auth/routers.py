from auth.auth import auth_backend, fastapi_users
from auth.schemas import UserCreate, UserRead
from fastapi import APIRouter


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
curred_user = fastapi_users.current_user()
