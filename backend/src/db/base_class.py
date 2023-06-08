from sqlalchemy import Column, Integer

from sqlalchemy.orm import declarative_base, declared_attr


class PreBase:
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        """Создает в моделях-наследниках свойство __tablename__ из
        имени модели, переведённого в нижний регистр.
        """
        return cls.__name__.lower()


Base = declarative_base(cls=PreBase)
