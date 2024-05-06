from flask import flash, redirect, render_template, request, url_for
from core.models.problem import Problem, ProblemTag
from core.database import db_session
from core.services import get_or_404
from core.validation.problem_new import ProblemNewForm
from core.services import problem as problem_service


def view(id):
    problem = get_or_404(Problem.query, id)
    return render_template("problem-view.jinja", problem=problem)


def edit(id, form=None):
    problem = get_or_404(Problem.query, id)
    tags = ProblemTag.query.all()
    if not form:
        form = ProblemNewForm(obj=problem)
        form.status.data = problem.status.name

    return render_template("problem-form.jinja",
                           form=form,
                           contest=problem.contest,
                           problem=problem,
                           tags=tags,
                           mode_edit=True
                           )


def update(id):
    problem = get_or_404(Problem.query, id)
    form = ProblemNewForm(request.form)
    if not form.validate():
        return edit(id, form)
    problem_service.edit(problem, form)
    flash('Изменения сохранены!', "success")
    return redirect(url_for('problem.view', id=id))


def delete(id):
    get_or_404(Problem.query, id)
    Problem.query.filter(Problem.id == id).delete()
    db_session.commit()
    flash("Задача удалена!", "success")
    return '', 204
