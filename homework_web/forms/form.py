from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField, RadioField, \
    widgets
from wtforms.validators import DataRequired
from wtforms import SelectMultipleField
from wtforms import validators


class ContestantForm(FlaskForm):
    surname = StringField(validators=[DataRequired("Enter your surname")])
    name = StringField(validators=[DataRequired("Enter your name")])
    email = StringField("Почта", validators=[DataRequired()])
    education = SelectField("Образование", choices=[('нач', 'Начальное'), ("ср", "Среднее"), ("выс", "Высшее")])
    motivation = TextAreaField("Мотивация", validators=[DataRequired()])
    gender = RadioField("Пол", choices=[("M", "Мужчина"), ("F", "Женщина")])
    job = SelectMultipleField("Профессия", choices=[(1, 'Инжене-исследователь'), (2, 'Инженер-Строитель'),
                                                    (3, 'Пилот'), (4, 'Метеоролог'), (5, 'Инженер по жизнеобеспечению'),
                                                    (6, 'Инженер по радиоционной защите'),
                                                    (7, 'Врач'), (8, 'Экзобиолог')],
                              widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2])
    ready = BooleanField("Готовы остаться на Марсе?")
    submit = SubmitField("Отправить")
