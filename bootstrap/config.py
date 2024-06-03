import os
import re
from dotenv import dotenv_values
from flask.cli import load_dotenv

app_config = {}


def prepare_config():
    load_dotenv()

    global app_config

    app_config = dotenv_values(".env")
    if app_config['DATABASE_URL'].startswith('sqlite'):
        _sqlite_prepare_directories(app_config['DATABASE_URL'])


def _sqlite_prepare_directories(path):
    db_file = re.sub("sqlite.*:///", "", path)
    os.makedirs(os.path.dirname(db_file), exist_ok=True)
