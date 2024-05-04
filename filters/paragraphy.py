def paragraphy(text):
    paragraphs = text.split('\n')
    wrapped_text = ''
    for paragraph in paragraphs:
        if paragraph.strip():
            wrapped_text += f'<p>{paragraph.strip()}</p>'
        else:
            wrapped_text += '<br />'
    return wrapped_text
