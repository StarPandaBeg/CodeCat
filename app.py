from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SERVER_NAME'] = "localhost:5000"

    return app


app = create_app()
