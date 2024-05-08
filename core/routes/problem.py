from flask import Blueprint
from core.controllers import problem

bp = Blueprint('problem', __name__, url_prefix='/problems')

bp.route("/")(problem.index)
bp.route("/<id>")(problem.view)
bp.get('/new')(problem.create)
bp.post('/new')(problem.store)
bp.get("/<id>/edit")(problem.edit)
bp.post("/<id>/edit")(problem.update)
bp.delete("/<id>")(problem.delete)

bp.post("/search")(problem.search)
