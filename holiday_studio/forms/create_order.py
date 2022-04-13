from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, TelField, EmailField
from wtforms.validators import DataRequired


class CreateOrderForm(FlaskForm):
    title = StringField("Название заказа", validators =[DataRequired()])
    price = IntegerField("tcena", validators=[])
    descroption = StringField("Описание", validators =[DataRequired()])
    submit = SubmitField("оздать заказ")