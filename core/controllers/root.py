from flask import redirect, url_for


def index():
    return redirect(url_for('contest.index'))
