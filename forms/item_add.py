from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class ItemForm(FlaskForm):
    name = StringField("Название предмета", validators=[DataRequired()], render_kw={
        "class": "input-str form-control",
        "required": True,
    })

    image = FileField('Картинка', validators=[DataRequired()], render_kw={
        "required": True,
    })

    submit = SubmitField('Отправить')
