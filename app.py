from flask import Flask
from core.database import db_session, init_db
from filters import init_jinja_filters
from core.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['SERVER_NAME'] = "localhost:5000"
    app.template_folder = 'core/views'
    register_routes(app)

    return app


app = create_app()
init_db()
init_jinja_filters(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
