class StudentLessonAssoc:  # 2 +
    first_id: int
    second_id: int

    first: Mapped["First"] = relationship()
    second: Mapped["Second"] = relationship()

# 0 0 0
# 0 0 1
# 0 1 0
# 1 0 0
# 0 1 1
# 1 1 1
# 1 0 1
