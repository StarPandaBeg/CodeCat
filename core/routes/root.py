from flask import Blueprint
import core.controllers.root as root

bp = Blueprint('root', __name__)

bp.route('/')(root.index)
