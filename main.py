from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column,
    sessionmaker,
)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__}".lower()


class User(Base):
    login: Mapped[str]
    password: Mapped[str]


class Config:
    ENGINE = create_engine("sqlite://", echo=True)
    BASE = Base
    SESSION = sessionmaker(bind=ENGINE)

    @classmethod
    def up(cls):
        cls.BASE.metadata.create_all(cls.ENGINE)

    @classmethod
    def down(cls):
        cls.BASE.metadata.drop_all(cls.ENGINE)


def main():
    Config.up()
    user = User(login="Acuta", password="Acuta")
    with Config.SESSION.begin() as session:
        session.add(user)


if __name__ == "__main__":
    main()
