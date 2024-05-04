from flask import Flask
import blueprints.contest as bp_contest


def create_app():
    app = Flask(__name__)
    app.config['SERVER_NAME'] = "localhost:5000"
    app.register_blueprint(bp_contest.bp)

    return app


app = create_app()
