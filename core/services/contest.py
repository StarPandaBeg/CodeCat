from core.models.contest import Contest
from core.models.problem import Problem
from core.validation.contest_delete import ContestDeleteForm
from core.validation.contest_new import ContestNewForm
from core.database import db_session


def create(form: ContestNewForm):
    contest = Contest(
        name=form.name.data,
        date=form.date.data,
        link=form.link.data,
        description=form.description.data
    )
    db_session.add(contest)
    db_session.commit()
    return contest


def edit(contest: Contest, form: ContestNewForm):
    form.populate_obj(contest)
    db_session.commit()


def delete(id: int, form: ContestDeleteForm):
    if form.delete_problems.data:
        Problem.query.filter(Problem.contest_id == id).delete()
    Contest.query.filter(Contest.id == id).delete()
    db_session.commit()
