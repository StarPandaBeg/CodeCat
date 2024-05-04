from flask import Flask
import blueprints.contest as bp_contest
import blueprints.problem as bp_problem


def create_app():
    app = Flask(__name__)
    app.config['SERVER_NAME'] = "localhost:5000"
    app.register_blueprint(bp_contest.bp)
    app.register_blueprint(bp_problem.bp)

    return app


app = create_app()
