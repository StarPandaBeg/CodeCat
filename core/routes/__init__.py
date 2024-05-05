from flask import Blueprint, Flask
from .contest import bp as contest_bp

_blueprints: list[Blueprint] = [
    contest_bp
]


def register_routes(app: Flask):
    for bp in _blueprints:
        app.register_blueprint(bp)
