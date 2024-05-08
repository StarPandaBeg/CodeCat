from markdown import markdown as md

_replacements = [
    ('\r\n', '\n'),

    # Add <br> to force empty lines
    ('\n\n', '\n\n<br>\n\n'),
]


def markdown(text):
    _text = _prepare(text)
    return md(_text)


def _prepare(text):
    # Prevent html escaping when Markup object passed
    _text = str(text)
    for r in _replacements:
        _text = _text.replace(*r)
    return _text
