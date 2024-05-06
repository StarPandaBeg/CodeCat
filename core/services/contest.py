from core.models.contest import Contest
from core.validation.contest_new import ContestNewForm
from database import db_session


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
