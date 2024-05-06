from flask import Blueprint, Flask
from .contest import bp as contest_bp
from .problem import bp as problem_bp

_blueprints: list[Blueprint] = [
    contest_bp,
    problem_bp
]


def register_routes(app: Flask):
    for bp in _blueprints:
        app.register_blueprint(bp)
