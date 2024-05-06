from flask import Blueprint
from core.controllers import problem

bp = Blueprint('problem', __name__, url_prefix='/problems')

bp.route("/<id>")(problem.view)
