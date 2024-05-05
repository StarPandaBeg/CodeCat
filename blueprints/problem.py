from flask import Blueprint, render_template

from core.models.problem import Problem

bp = Blueprint("problem", __name__, url_prefix="/problems")


@bp.route("/<id>")
def view(id):
    problem = Problem.query.get(id)
    return render_template("problem-view.jinja", problem=problem)
