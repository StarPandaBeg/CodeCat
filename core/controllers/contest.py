from flask import flash, redirect, render_template, request, url_for

from core.models.contest import Contest
from core.validation.contest_new import ContestNewForm
import core.services.contest as contest_service


def index():
    contests = Contest.query.all()
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
