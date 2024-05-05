from flask import Blueprint, flash, redirect, render_template, request, url_for
from core.models.problem import Problem, ProblemExample, ProblemSolution, ProblemTag
from core.models.contest import Contest
from validation.contest_new import ContestNewForm
from database import db_session
from validation.problem_new import ProblemNewForm

bp = Blueprint("contest", __name__, url_prefix="/contests")


@bp.route("/")
def index():
    contests = Contest.query.all()
    return render_template("contest-list.jinja", contests=contests)


@bp.get('/new')
def create_get():
    form = ContestNewForm(request.form)
    return render_template("contest-new.jinja", form=form)


@bp.post('/new')
def create_post():
    form = ContestNewForm(request.form)
    if form.validate():
        contest = Contest(
            name=form.name.data,
            date=form.date.data,
            link=form.link.data,
            description=form.description.data
        )
        db_session.add(contest)
        db_session.commit()
        flash('Соревнование создано!', 'success')
        return redirect(url_for('contest.view', id=contest.id))
    return render_template("contest-new.jinja", form=form)


@bp.route("/<id>")
def view(id):
    contest = Contest.query.get(id)
    return render_template("contest-view.jinja", contest=contest)


@bp.get("/<id>/new")
def create_problem_get(id):
    contest = Contest.query.get(id)
    form = ProblemNewForm()
    tags = ProblemTag.query.all()
    return render_template("problem-new.jinja", contest=contest, form=form, tags=tags)


@bp.post("/<id>/new")
def create_problem_post(id):
    contest = Contest.query.get(id)
    tags = ProblemTag.query.all()
    form = ProblemNewForm(request.form)

    tags_to_add = []

    if form.validate():
        problem = Problem(
            name=form.name.data,
            letter=form.letter.data,
            time_limit=form.time_limit.data,
            memory_limit=form.memory_limit.data,
            status=form.status.data,
            text=form.text.data,
            data_in=form.data_in.data,
            data_out=form.data_out.data
        )
        for ex in form.examples:
            example = ProblemExample(
                input=ex.input.data, output=ex.output.data)
            problem.examples.append(example)
        for sol in form.solutions:
            solution = ProblemSolution(
                code=sol.code.data, lang=sol.lang.data, comment=sol.comment.data)
            problem.solutions.append(solution)

        for tag in form.tags.data:
            found = next((x for x in tags if x.tag == tag), None)
            if found:
                problem.tags.append(found)
            else:
                tagobj = ProblemTag(tag=tag)
                db_session.add(tagobj)
                tags_to_add.append(tagobj)

        contest.problems.append(problem)
        db_session.commit()

        for tag in tags_to_add:
            problem.tags.append(tag)
        db_session.commit()

        flash('Задача создана!', 'success')
        return redirect(url_for('contest.view', id=contest.id))
    return render_template("problem-new.jinja", contest=contest, form=form, tags=tags)
