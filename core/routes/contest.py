from flask import Blueprint

bp = Blueprint('contest', __name__, url_prefix='/contests')

bp.route('/')(lambda: "Hello!")
