from sqlalchemy import Column, Integer
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base, declared_attr

metadata = MetaData()


class PreBase:
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        """Создает в моделях-наследниках свойство __tablename__ из
        имени модели, переведённого в нижний регистр.
        """
        return cls.__name__.lower()


Base = declarative_base(cls=PreBase)
