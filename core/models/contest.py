from typing import List
from database import Base
from sqlalchemy import Integer, String, Date, Text
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

    problems: Mapped[List["Problem"]] = relationship(back_populates="contest")
