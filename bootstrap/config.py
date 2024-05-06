import json
from os import path
import os
import re

app_config = {}


class ConfigError(Exception):
    pass


def prepare_config():
    global app_config

    _prepare_config('flask')
    _prepare_config('app', True)

    with open(f"config/app.json", 'r', encoding='utf-8') as f:
        app_config = json.load(f)

    if app_config['DATABASE_URL'].startswith('sqlite'):
        _sqlite_prepare_directories(app_config['DATABASE_URL'])


def _prepare_config(filename: str, ignore_example: bool = True):
    if path.exists(f"config/{filename}.json"):
        return
    if path.exists(f"config/{filename}.example.json"):
        os.rename(f"config/{filename}.example.json",
                  f"config/{filename}.json")
        if not ignore_example:
            raise ConfigError(
                f"Please configure application - example config file `{filename}.json` was successfully created")

    with open(f"config/{filename}.json") as f:
        f.write("{}")
    raise ConfigError(
        f"Please configure application - create file `{filename}.json` (example file isn't found so you need to do it manually)")


def _sqlite_prepare_directories(path):
    db_file = re.sub("sqlite.*:///", "", path)
    os.makedirs(os.path.dirname(db_file), exist_ok=True)
