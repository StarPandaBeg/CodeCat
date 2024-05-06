from typing import List

from sqlalchemy import select, text

from core.models.contest import Contest
from core.models.problem import Problem, ProblemExample, ProblemFTS, ProblemSolution, ProblemTag
from core.validation.problem_new import ProblemNewForm
from core.database import db_session


def create(form: ProblemNewForm, contest: Contest | None = None):
    tags: List[ProblemTag] = ProblemTag.query.all()
    problem = Problem(
        name=form.name.data,
        letter=form.letter.data,
        time_limit=form.time_limit.data,
        memory_limit=form.memory_limit.data,
        status=form.status.data,
        text=form.text.data,
        data_in=form.data_in.data,
        data_out=form.data_out.data,
        example_description=form.example_description.data
    )
    _createProblemExamples(problem, form.examples.data)
    _createProblemSolutions(problem, form.solutions.data)

    tags_to_add = _assignProblemTags(problem, form.tags.data, tags)
    for tag in tags_to_add:
        tagModel = ProblemTag(tag=tag)
        problem.tags.append(tagModel)
        db_session.add(tagModel)

    if (contest):
        contest.problems.append(problem)
    else:
        db_session.add(problem)
    db_session.commit()


def edit(problem: Problem, form: ProblemNewForm):
    # Tags will be processed manually
    tags: List[ProblemTag] = ProblemTag.query.all()
    problem.tags.clear()
    tags_to_add = _assignProblemTags(problem, form.tags.data, tags)
    for tag in tags_to_add:
        tagModel = ProblemTag(tag=tag)
        problem.tags.append(tagModel)
        db_session.add(tagModel)
    del form.tags

    # Due to issues with removed items population, it's easier to remove all related objects and create new ones
    ProblemExample.query.filter(
        ProblemExample.problem_id == problem.id).delete()
    ProblemSolution.query.filter(
        ProblemSolution.problem_id == problem.id).delete()

    form.populate_obj(problem)
    db_session.commit()


def search(query: str):
    fts_stmt = select(ProblemFTS.id).where(
        text(ProblemFTS.__tablename__ + f" MATCH '{query}'")
    )
    return Problem.query.where(Problem.id.in_(fts_stmt)).all()


def _createProblemExamples(problem: Problem, examples: list[dict[str, str]]):
    # TODO: Impove typing - idk how to implement it there
    for example in examples:
        exampleModel = ProblemExample(
            input=example['input'],
            output=example['output']
        )
        problem.examples.append(exampleModel)


def _createProblemSolutions(problem: Problem, solutions: list[dict[str, str]]):
    # TODO: Impove typing - idk how to implement it there
    for solution in solutions:
        solutionModel = ProblemSolution(
            code=solution['code'],
            lang=solution['lang'],
            comment=solution['comment']
        )
        problem.solutions.append(solutionModel)


def _assignProblemTags(problem: Problem, tags_raw: List[str], tags: List[ProblemTag]):
    unknown_tags: List[str] = []
    for tag in tags_raw:
        found = next((x for x in tags if x.tag == tag), None)
        if found:
            problem.tags.append(found)
        else:
            unknown_tags.append(tag)
    return unknown_tags
