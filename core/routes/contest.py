from flask import Blueprint
import core.controllers.contest as contest

bp = Blueprint('contest', __name__, url_prefix='/contests')

bp.route('/')(contest.index)
bp.route('/<id>')(contest.view)
