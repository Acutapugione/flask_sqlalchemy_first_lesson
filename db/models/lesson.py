from datetime import datetime
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import ForeignKey
from . import Config


class Lesson(Config.BASE):
    """represents lesson data"""

    topic: Mapped[str]
    timestamp: Mapped[datetime]

    teacher_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    teacher: Mapped["User"] = relationship(back_populates="lessons")
    # students: Mapped[list["Student"]]
