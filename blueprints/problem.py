from flask import Blueprint, render_template

bp = Blueprint("problem", __name__, url_prefix="/problems")


@bp.route("/<id>")
def view(id):
    return render_template("problem-view.jinja", id=id)
