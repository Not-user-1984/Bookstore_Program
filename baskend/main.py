from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def create_tables():
	print("create_tables")
	Base.metadata.create_all(bind=engine)


def start_application():
	create_tables()
	return app

app = start_application()
