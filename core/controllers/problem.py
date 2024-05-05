from flask import render_template
from core.models.problem import Problem


def view(id):
    problem = Problem.query.get(id)
    return render_template("problem-view.jinja", problem=problem)
