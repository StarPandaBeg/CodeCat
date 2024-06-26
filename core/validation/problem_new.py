from wtforms import FieldList, FormField, SelectField, StringField, TextAreaField, ValidationError, validators
from core.models.problem import ProblemExample, ProblemSolution
from core.util.status import get_problemstatus_items
from .base import FormBase


class ProblemExampleNewForm(FormBase):
    input = TextAreaField('input', [validators.DataRequired()])
    output = TextAreaField('output', [validators.DataRequired()])


class ProblemSolutionNewForm(FormBase):
    code = TextAreaField('code', [validators.DataRequired()])
    lang = StringField('lang', [validators.DataRequired()])
    comment = TextAreaField('comment')


class ProblemNewForm(FormBase):
    name = StringField('name', [validators.Length(min=4, max=64)])
    letter = StringField('letter', validators=[
        validators.Optional(),
        validators.Length(min=1, max=4),
        validators.Regexp(r'^[a-zA-Z]{1,4}$')
    ])
    time_limit = StringField('time_limit', [validators.Length(min=4, max=16)])
    memory_limit = StringField(
        'memory_limit', [validators.Length(min=4, max=16)])
    status = SelectField(
        'status', choices=get_problemstatus_items(), default='none')
    text = TextAreaField('text')
    data_in = TextAreaField('data_in')
    data_out = TextAreaField('data_out')
    example_description = TextAreaField('example_description')
    link = StringField('link', [validators.Optional(), validators.URL()])

    examples = FieldList(FormField(ProblemExampleNewForm,
                                   default=lambda: ProblemExample()))
    solutions = FieldList(FormField(ProblemSolutionNewForm,
                                    default=lambda: ProblemSolution()))
    tags = FieldList(StringField('tags'))

    def validate_examples(self, field):
        if len(field.data) == 0:
            raise ValidationError("Добавьте по крайней мере один пример")
