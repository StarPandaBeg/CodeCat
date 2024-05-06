from flask import flash, render_template
from core.models.problem import Problem
from core.database import db_session


def view(id):
    problem = Problem.query.get(id)
    return render_template("problem-view.jinja", problem=problem)


def delete(id):
    Problem.query.filter(Problem.id == id).delete()
    db_session.commit()
    flash("Задача удалена!", "success")
    return '', 204
