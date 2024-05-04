from __future__ import annotations

import enum
from database import Base
from sqlalchemy import Enum, ForeignKey, Integer, String, Text, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

import typing

if typing.TYPE_CHECKING:
    from models.contest import Contest

tag_association_table = Table(
    "problem_tags",
    Base.metadata,
    Column("problem_id", ForeignKey("problems.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)


class ProblemStatus(enum.Enum):
    none = 0
    solved = 1
    wrong = 2
    time_exceed = 3
    memory_exceed = 4


class Problem(Base):
    __tablename__ = 'problems'

    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, autoincrement=True)
    contest_id: Mapped[int] = mapped_column(ForeignKey("contests.id"))
    letter: Mapped[str] = mapped_column(String(4), nullable=False)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    time_limit: Mapped[str] = mapped_column(String(16))
    memory_limit: Mapped[str] = mapped_column(String(16))
    status: Mapped[ProblemStatus] = mapped_column(Enum(ProblemStatus))
    text: Mapped[str] = mapped_column(Text())
    data_in: Mapped[str] = mapped_column(Text())
    data_out: Mapped[str] = mapped_column(Text())

    contest: Mapped["Contest"] = relationship(back_populates="problems")

    tags: Mapped[List[ProblemTag]] = relationship(
        secondary=tag_association_table, back_populates="problems"
    )

    @property
    def css_class(self):
        match self.status.value:
            case ProblemStatus.solved.value:
                return "solved"
            case ProblemStatus.time_exceed.value | ProblemStatus.memory_exceed.value | ProblemStatus.wrong.value:
                return "failed"
            case _:
                return ''


class ProblemTag(Base):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, autoincrement=True)
    tag: Mapped[str] = mapped_column(String(64), nullable=False)
    problems: Mapped[List[Problem]] = relationship(
        secondary=tag_association_table, back_populates="tags"
    )
