from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class ItemForm(FlaskForm):
    label = 'Название предмета'
    name = StringField(label, validators=[DataRequired()], render_kw={
        "class": "input-str form-control",
        "required": True,
        "placeholder": label
    })

    label = 'Картинка'
    image = FileField(label, validators=[DataRequired()], render_kw={
        "required": True,
        "placeholder": label
    })

    submit = SubmitField('Отправить')
