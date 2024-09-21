from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base


class Config:
    ENGINE = create_engine("sqlite:///my.db", echo=True)
    BASE = Base
    SESSION = sessionmaker(bind=ENGINE)

    @classmethod
    def up(cls):
        cls.BASE.metadata.create_all(cls.ENGINE)

    @classmethod
    def down(cls):
        cls.BASE.metadata.drop_all(cls.ENGINE)
