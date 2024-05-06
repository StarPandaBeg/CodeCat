from flask import Blueprint
from core.controllers import problem

bp = Blueprint('problem', __name__, url_prefix='/problems')

bp.route("/<id>")(problem.view)
bp.get("/<id>/edit")(problem.edit)
bp.post("/<id>/edit")(problem.update)
bp.delete("/<id>")(problem.delete)
