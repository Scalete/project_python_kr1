from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class NumberForm(FlaskForm):
    number = IntegerField('Введіть ціле позитивне число', validators=[
        DataRequired(message="Поле не повинно бути порожнім"),
        NumberRange(min=0, message="Введіть додатне ціле число")
    ])
    submit = SubmitField('Перевірити')