from __future__ import annotations

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING
from core.util.status import ProblemStatus
from core.database import Base, Base2, CreateFtsTable

if TYPE_CHECKING:
    from core.models.contest import Contest

tag_association_table = sa.Table(
    "problem_tags",
    Base.metadata,
    sa.Column("problem_id", sa.ForeignKey("problems.id",
                                          ondelete='CASCADE'), primary_key=True),
    sa.Column("tag_id", sa.ForeignKey(
        "tags.id", ondelete='CASCADE'), primary_key=True),
)


class Problem(Base):
    __tablename__ = 'problems'

    id: Mapped[int] = mapped_column(
        sa.Integer(), primary_key=True, autoincrement=True)
    contest_id: Mapped[int] = mapped_column(sa.ForeignKey(
        "contests.id", ondelete='SET NULL'), nullable=True)
    letter: Mapped[str] = mapped_column(sa.String(4), nullable=False)
    name: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    time_limit: Mapped[str] = mapped_column(sa.String(16))
    memory_limit: Mapped[str] = mapped_column(sa.String(16))
    status: Mapped[ProblemStatus] = mapped_column(sa.Enum(ProblemStatus))
    text: Mapped[str] = mapped_column(sa.Text())
    data_in: Mapped[str] = mapped_column(sa.Text())
    data_out: Mapped[str] = mapped_column(sa.Text())

    contest: Mapped["Contest"] = relationship(back_populates="problems")

    tags: Mapped[List[ProblemTag]] = relationship(
        secondary=tag_association_table, back_populates="problems", order_by=sa.column("tag")
    )
    examples: Mapped[List[ProblemExample]] = relationship(
        back_populates="problem", order_by=sa.column("id")
    )
    example_description: Mapped[str] = mapped_column(sa.Text())
    solutions: Mapped[List[ProblemSolution]] = relationship(
        back_populates="problem", order_by=sa.column("id")
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
        sa.Integer(), primary_key=True, autoincrement=True)
    tag: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    problems: Mapped[List[Problem]] = relationship(
        secondary=tag_association_table, back_populates="tags"
    )


class ProblemExample(Base):
    __tablename__ = 'problem_examples'

    id: Mapped[int] = mapped_column(
        sa.Integer(), primary_key=True, autoincrement=True)
    problem_id: Mapped[int] = mapped_column(
        sa.ForeignKey("problems.id", ondelete='CASCADE'))
    input:  Mapped[str] = mapped_column(sa.Text(), nullable=False)
    output:  Mapped[str] = mapped_column(sa.Text(), nullable=False)

    problem: Mapped[Problem] = relationship(back_populates="examples")


class ProblemSolution(Base):
    __tablename__ = 'problem_solutions'

    id: Mapped[int] = mapped_column(
        sa.Integer(), primary_key=True, autoincrement=True)
    problem_id: Mapped[int] = mapped_column(
        sa.ForeignKey("problems.id", ondelete='CASCADE'))
    code: Mapped[str] = mapped_column(sa.Text(), nullable=False)
    lang: Mapped[str] = mapped_column(sa.String(16), nullable=False)
    comment: Mapped[str] = mapped_column(sa.Text())

    problem: Mapped[Problem] = relationship(back_populates="solutions")


class ProblemFTS(Base2):
    __tablename__ = 'problems_idx'

    id: Mapped[int] = mapped_column(
        sa.Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    text: Mapped[str] = mapped_column(sa.Text(), nullable=False)


update_fts = sa.DDL('''CREATE TRIGGER problem_fts_update AFTER INSERT ON problems
  BEGIN
    INSERT INTO problems_idx (id, name, sa.Text) 
    VALUES (new.id, new.name, new.sa.Text);
  END;''')
sa.event.listen(Problem.__table__, 'after_create', CreateFtsTable(ProblemFTS))
sa.event.listen(Problem.__table__, 'after_create', update_fts)
