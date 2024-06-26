from flask import flash, redirect, render_template, request, url_for, abort
from core.models.problem import Problem, ProblemTag
from core.database import db_session
from core.services import get_or_404
from core.validation.problem_new import ProblemNewForm
from core.services import problem as problem_service
from core.util.pagination import Pagination


def index():
    page = request.args.get('page', 1, int)
    stmt = Problem.query.order_by(Problem.id.desc())

    pagination = Pagination(page)
    pagination.set_stmt(stmt)

    problems = pagination.paginate()
    return render_template("problem-index.jinja", problems=problems, pag=pagination)


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


def search():
    query = request.form.get('query', 'no')
    if not query:
        return redirect(url_for('problem.index'))
    problems = problem_service.search(query)
    return render_template("problem-index.jinja", problems=problems, query=query, mode_search=True)


def create():
    tags = ProblemTag.query.all()
    form = ProblemNewForm()
    return render_template("problem-form.jinja", form=form, tags=tags)


def store():
    form = ProblemNewForm(request.form)
    if not form.validate():
        return create()
    problem_service.create(form)
    flash('Задача создана!', "success")
    return redirect(url_for('problem.index'))
