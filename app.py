# Configuration must be loaded very early
from bootstrap.config import prepare_config
prepare_config()  # noqa

from filters import init_jinja_filters
from core.routes import register_routes
from core.database import db_session, init_db
from flask import Flask


def create_flask_app():
    app = Flask(__name__)
    app.template_folder = 'core/views'

    _import_flask_config(app)
    register_routes(app)
    init_jinja_filters(app)

    return app


def _import_flask_config(app: Flask):
    app.config.from_prefixed_env()


app = create_flask_app()
init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
