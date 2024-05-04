from flask import Blueprint, redirect, render_template, request, url_for
from models.contest import Contest
from validation.contest_new import ContestNewForm
from database import db_session

bp = Blueprint("contest", __name__, url_prefix="/contests")


@bp.route("/")
def index():
    contests = Contest.query.all()
    return render_template("contest-list.jinja", contests=contests)


@bp.get('/new')
def create_get():
    form = ContestNewForm(request.form)
    return render_template("contest-new.jinja", form=form)


@bp.post('/new')
def create_post():
    form = ContestNewForm(request.form)
    if form.validate():
        contest = Contest(
            name=form.name.data,
            date=form.date.data,
            link=form.link.data,
            description=form.description.data
        )
        db_session.add(contest)
        db_session.commit()
        return redirect(url_for('contest.view', id=contest.id))
    return render_template("contest-new.jinja", form=form)


@bp.route("/<id>")
def view(id):
    contest = Contest.query.get(id)
    return render_template("contest-view.jinja", contest=contest)
