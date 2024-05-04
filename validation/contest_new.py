from wtforms import StringField, DateField, TextAreaField, URLField, ValidationError, validators
from validation.base import FormBase
from datetime import date


class ContestNewForm(FormBase):
    name = StringField('name', [validators.Length(min=4, max=64)])
    date = DateField('date', render_kw={'max': date.today()})
    link = URLField('link', [validators.Optional(), validators.URL()])
    description = TextAreaField('description')

    def validate_date(self, field):
        try:
            today = date.today()
            actual = field.data
            if (actual > today):
                raise ValidationError("Дата не может быть в будущем")
        except ValidationError:
            raise
        except Exception as e:
            raise ValidationError("Неверная дата")
