from flask_wtf import FlaskForm
from wtforms import HiddenField, RadioField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import AnyOf, DataRequired, NumberRange


class EndlessOrangeSettingsForm(FlaskForm):
    mode = HiddenField(validators=[DataRequired(), AnyOf(["endless-orange"])])
    time = IntegerRangeField(validators=[DataRequired(), NumberRange(min=1, max=6)])
    rounds = IntegerRangeField(validators=[DataRequired(), NumberRange(min=1, max=20)])
    question_type = RadioField(choices=["dci", "both-dci-tips", "tips"], validators=[DataRequired()])
    communication_type = RadioField(choices=["host", "both-host-team", "team"], validators=[DataRequired()])
