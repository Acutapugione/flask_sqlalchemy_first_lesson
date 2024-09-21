from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column,
    relationship,
)
from . import Config


class User(Config.BASE):
    login: Mapped[str]
    password: Mapped[str]
    lessons: Mapped[list["Lesson"]] = relationship(back_populates="teacher")
