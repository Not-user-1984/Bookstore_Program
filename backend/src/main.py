from fastapi import FastAPI

from api.routers import main_router
from config import settings

app = FastAPI(
    title=settings.app_title,
    description=settings.description,
)

app.include_router(main_router)

# допилить регистaрцию разобраться со созданием user