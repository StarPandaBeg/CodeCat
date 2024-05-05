from flask import render_template
from core.models.contest import Contest


def index():
    contests = Contest.query.all()
    return render_template("contest-index.jinja", contests=contests)


def view(id):
    contest = Contest.query.get(id)
    return render_template("contest-view.jinja", contest=contest)
