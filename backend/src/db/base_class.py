from sqlalchemy import Column, Integer
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData()


class PreBase:
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)
