from flask import abort, flash, redirect, render_template, request, url_for

from core.models.contest import Contest
from core.models.problem import ProblemTag
from core.services import get_or_404
from core.validation.contest_delete import ContestDeleteForm
from core.validation.contest_new import ContestNewForm
from core.validation.problem_new import ProblemNewForm
import core.services.contest as contest_service
import core.services.problem as problem_service


def index():
    contests = Contest.query.order_by(Contest.date.desc()).all()
    return render_template("contest-index.jinja", contests=contests)


def view(id):
    contest = get_or_404(Contest.query, id)
    return render_template("contest-view.jinja", contest=contest)


def create():
    form = ContestNewForm()
    return render_template("contest-form.jinja", form=form)


def store():
    form = ContestNewForm(request.form)
    if not form.validate():
        return render_template("contest-form.jinja", form=form)
    contest = contest_service.create(form)
    flash('Соревнование создано!', 'success')
    return redirect(url_for('contest.view', id=contest.id))


def edit(id, form=None):
    contest = get_or_404(Contest.query, id)
    if not form:
        form = ContestNewForm(obj=contest)
    return render_template("contest-form.jinja", form=form, contest=contest, mode_edit=True)


def update(id):
    contest = get_or_404(Contest.query, id)
    form = ContestNewForm(request.form)
    if not form.validate():
        return edit(id, form)
    contest_service.edit(contest, form)
    return redirect(url_for('contest.view', id=id))


def delete(id):
    get_or_404(Contest.query, id)
    form = ContestDeleteForm(request.form)
    if not form.validate():
        return abort(400)
    contest_service.delete(id, form)
    flash('Соревнование удалено!', "success")
    if not form.delete_problems.data:
        flash('Задачи перенесены в категорию <Без соревнования>', "info")
    return '', 204


def search():
    query = request.form.get('query', 'no')
    if not query:
        abort(400)
    contests = contest_service.search(query)
    return render_template("contest-index.jinja", contests=contests, mode_search=True, query=query)


def create_problem(id):
    contest = get_or_404(Contest.query, id)
    tags = ProblemTag.query.all()
    form = ProblemNewForm()
    return render_template("problem-form.jinja", form=form, contest=contest, tags=tags)


def store_problem(id):
    contest = get_or_404(Contest.query, id)
    form = ProblemNewForm(request.form)
    if not form.validate():
        tags = ProblemTag.query.all()
        return render_template("problem-form.jinja", form=form, contest=contest, tags=tags)
    problem_service.create(form, contest)
    return redirect(url_for('contest.view', id=contest.id))
