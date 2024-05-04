from flask import Blueprint, render_template

bp = Blueprint("contest", __name__, url_prefix="/contests")


@bp.route("/")
def index():
    return render_template("contest-list.jinja")


@bp.route("/<id>")
def view(id):
    return render_template("contest-view.jinja", id=id)
