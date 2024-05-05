from flask import render_template
from core.models.contest import Contest


def index():
    contests = Contest.query.all()
    return render_template("contest-index.jinja", contests=contests)
