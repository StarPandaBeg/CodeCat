from flask import flash, render_template
from core.models.problem import Problem
from core.database import db_session
from core.services import get_or_404


def view(id):
    problem = get_or_404(Problem.query, id)
    return render_template("problem-view.jinja", problem=problem)


def delete(id):
    get_or_404(Problem.query, id)
    Problem.query.filter(Problem.id == id).delete()
    db_session.commit()
    flash("Задача удалена!", "success")
    return '', 204
