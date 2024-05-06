from wtforms import BooleanField
from core.validation.base import FormBase


class ContestDeleteForm(FormBase):
    delete_problems = BooleanField('delete_problems')
