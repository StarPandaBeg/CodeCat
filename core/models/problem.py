from __future__ import annotations

from sqlalchemy import Enum, ForeignKey, Integer, String, Text, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING
from core.util.status import ProblemStatus
from database import Base

if TYPE_CHECKING:
    from core.models.contest import Contest

tag_association_table = Table(
    "problem_tags",
    Base.metadata,
    Column("problem_id", ForeignKey("problems.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)


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
    examples: Mapped[List[ProblemExample]] = relationship(
        back_populates="problem"
    )
    example_description: Mapped[str] = mapped_column(Text())
    solutions: Mapped[List[ProblemSolution]] = relationship(
        back_populates="problem"
    )

    @property
    def css_class(self):
        match self.status.value:
            case ProblemStatus.solved.value:
                return "solved"
            case ProblemStatus.time_exceed.value | ProblemStatus.memory_exceed.value | ProblemStatus.wrong.value:
                return "failed"
            case _:
                return None

    @property
    def status_icon(self):
        match self.status.value:
            case ProblemStatus.solved.value:
                return "mdi-check-circle-outline"
            case ProblemStatus.time_exceed.value:
                return "mdi-clock-alert-outline"
            case ProblemStatus.memory_exceed.value:
                return "mdi-memory"
            case ProblemStatus.wrong.value:
                return "mdi-alert-circle-outline"
            case _:
                return None


class ProblemTag(Base):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, autoincrement=True)
    tag: Mapped[str] = mapped_column(String(64), nullable=False)
    problems: Mapped[List[Problem]] = relationship(
        secondary=tag_association_table, back_populates="tags"
    )


class ProblemExample(Base):
    __tablename__ = 'problem_examples'

    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, autoincrement=True)
    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id"))
    input:  Mapped[str] = mapped_column(Text(), nullable=False)
    output:  Mapped[str] = mapped_column(Text(), nullable=False)

    problem: Mapped[Problem] = relationship(back_populates="examples")


class ProblemSolution(Base):
    __tablename__ = 'problem_solutions'

    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, autoincrement=True)
    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id"))
    code: Mapped[str] = mapped_column(Text(), nullable=False)
    lang: Mapped[str] = mapped_column(String(16), nullable=False)
    comment: Mapped[str] = mapped_column(Text())

    problem: Mapped[Problem] = relationship(back_populates="solutions")
