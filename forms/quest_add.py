from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class QuestForm(FlaskForm):
    label = 'Вопрос'
    quest = StringField(label, validators=[DataRequired()], render_kw={
        "class": "input-str form-control",
        "required": True,
        "placeholder": label
    })

    image = BooleanField(label)
    erudition = BooleanField()
    leader = BooleanField(label)
    players = BooleanField(label)

    submit = SubmitField('Отправить')
