from flask import Flask
from database import db_session, init_db
import blueprints.contest as bp_contest
import blueprints.problem as bp_problem


def create_app():
    app = Flask(__name__)
    app.config['SERVER_NAME'] = "localhost:5000"
    app.register_blueprint(bp_contest.bp)
    app.register_blueprint(bp_problem.bp)

    return app


app = create_app()
init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
