from wtforms import PasswordField, StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.fields.html5 import EmailField, DateTimeLocalField
from wtforms.widgets.html5 import ColorInput
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    label = 'Email или имя пользователя'
    email = StringField(label, validators=[DataRequired()], render_kw={
        "class": "input-str form-control",
        "required": True,
        "placeholder": label
    })

    label = 'Пароль'
    password = PasswordField(label, validators=[DataRequired()], render_kw={
        "class": "input-str form-control",
        "type": "password",
        "required": True,
        "placeholder": label
    })

    submit = SubmitField('Войти')
