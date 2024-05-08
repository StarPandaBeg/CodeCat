from filters.paragraphy import paragraphy
from filters.markdown import markdown


def init_jinja_filters(app):
    app.jinja_env.filters['paragraphy'] = paragraphy
    app.jinja_env.filters['markdown'] = markdown
