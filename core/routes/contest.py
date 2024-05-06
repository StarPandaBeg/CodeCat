from flask import Blueprint
import core.controllers.contest as contest

bp = Blueprint('contest', __name__, url_prefix='/contests')

bp.route('/')(contest.index)
bp.route('/<id>')(contest.view)
bp.get('/new')(contest.create)
bp.post('/new')(contest.store)

bp.get('/<id>/new')(contest.create_problem)
bp.post('/<id>/new')(contest.store_problem)