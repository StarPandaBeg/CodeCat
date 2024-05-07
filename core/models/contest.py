from typing import List
from core.util.status import test_failed, test_solved, test_untouched
from core.database import Base
from sqlalchemy import Integer, String, Date, Text, column
from sqlalchemy.orm import Mapped, mapped_column, relationship

import typing

if typing.TYPE_CHECKING:
    from models.problem import Problem


class Contest(Base):
    __tablename__ = 'contests'

    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    date: Mapped[str] = mapped_column(Date())
    description: Mapped[str] = mapped_column(Text())
    link: Mapped[str] = mapped_column(String(64))

    problems: Mapped[List["Problem"]] = relationship(
        back_populates="contest", order_by=[column("letter"), column("name")])

    @property
    def problem_stats(self):
        return [
            sum(1 for problem in self.problems if test_solved(problem.status)),
            sum(1 for problem in self.problems if test_failed(problem.status)),
            sum(1 for problem in self.problems if test_untouched(problem.status)),
        ]
