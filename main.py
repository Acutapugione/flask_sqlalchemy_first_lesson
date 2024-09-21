from datetime import datetime
from sqlalchemy import select
from db import Config, User, Lesson


def main():
    Config.down()  # Comment for production
    Config.up()
    teacher = User(login="acutapugione", password="Acuta")
    teacher.lessons.extend(
        [
            Lesson(
                topic="Python Flask: Основи роботи з БД. СУБД",
                timestamp=datetime.now(),
            )
            for x in range(10)
        ]
    )
    with Config.SESSION.begin() as session:
        session.add(teacher)

    with Config.SESSION.begin() as session:
        sql_query = (
            select(Lesson.timestamp)
            .join(User, User.id == Lesson.teacher_id)
            .where(User.login.like(r"%acuta%"))
        )
        result = session.scalars(
            select(User).where(User.login.like(r"%acuta%"))
        ).first()
        print(f"{result=}")
        if result:
            print(f"{[lesson.timestamp for lesson in result.lessons]}")


if __name__ == "__main__":
    main()
