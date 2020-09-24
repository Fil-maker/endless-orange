from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class QuestForm(FlaskForm):

    label = "Вопрос"
    quest = StringField(label, validators=[DataRequired()], render_kw={
        "class": "input-str form-control",
        "required": True,
        "placeholder": label
    })

    label = "Воображение"
    image = BooleanField(label, render_kw={
        "class": "input-str form-control",
        "placeholder": label})

    label = "Эрудиция"
    erudition = BooleanField(label, render_kw={
        "class": "input-str form-control",
        "placeholder": label})

    label = "Только для ведущего"
    leader = BooleanField(label, render_kw={
        "class": "input-str form-control",
        "placeholder": label})

    label = "Для ведущего или игроков"
    players = BooleanField(label, render_kw={
        "class": "input-str form-control",
        "placeholder": label})

    submit = SubmitField('Отправить')
