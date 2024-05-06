from flask import flash, redirect, render_template, request, url_for

from core.models.contest import Contest
from core.models.problem import ProblemTag
from core.validation.contest_new import ContestNewForm
from core.validation.problem_new import ProblemNewForm
import core.services.contest as contest_service
import core.services.problem as problem_service


def index():
    contests = Contest.query.order_by(Contest.date.desc()).all()
    return render_template("contest-index.jinja", contests=contests)


def view(id):
    contest = Contest.query.get(id)
    return render_template("contest-view.jinja", contest=contest)


def create():
    form = ContestNewForm()
    return render_template("contest-create.jinja", form=form)


def store():
    form = ContestNewForm(request.form)
    if not form.validate():
        return render_template("contest-create.jinja", form=form)
    contest = contest_service.create(form)
    flash('Соревнование создано!', 'success')
    return redirect(url_for('contest.view', id=contest.id))


def create_problem(id):
    contest = Contest.query.get(id)
    tags = ProblemTag.query.all()
    form = ProblemNewForm()
    return render_template("problem-create.jinja", form=form, contest=contest, tags=tags)


def store_problem(id):
    contest = Contest.query.get(id)
    form = ProblemNewForm(request.form)
    if not form.validate():
        tags = ProblemTag.query.all()
        return render_template("problem-create.jinja", form=form, contest=contest, tags=tags)
    problem_service.create(form, contest)
    return redirect(url_for('contest.view', id=contest.id))
