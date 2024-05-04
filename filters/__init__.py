from filters.paragraphy import paragraphy


def init_jinja_filters(app):
    app.jinja_env.filters['paragraphy'] = paragraphy
