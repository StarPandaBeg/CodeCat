from flask import Blueprint, render_template
from models.contest import Contest

bp = Blueprint("contest", __name__, url_prefix="/contests")


@bp.route("/")
def index():
    contests = Contest.query.all()
    return render_template("contest-list.jinja", contests=contests)


@bp.route("/<id>")
def view(id):
    contest = Contest.query.get(id)
    return render_template("contest-view.jinja", contest=contest)
