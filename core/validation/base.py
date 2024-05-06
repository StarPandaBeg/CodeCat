from wtforms import Form


class FormBase(Form):
    class Meta:
        locales = ['ru_RU', 'ru']
