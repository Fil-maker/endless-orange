from flask_wtf import FlaskForm
from wtforms import HiddenField, RadioField
from wtforms.validators import AnyOf, DataRequired, NumberRange
from wtforms.fields.html5 import IntegerRangeField


class ThirdWheelSettingsForm(FlaskForm):
    mode = HiddenField(validators=[DataRequired(), AnyOf(["third-wheel"])])
    level = RadioField(choices=[1, 2, 3], validators=[DataRequired()])
    wheel_time = IntegerRangeField(validators=[DataRequired(), NumberRange(min=1, max=5)])
    wheel_rounds = IntegerRangeField(validators=[DataRequired(), NumberRange(min=1, max=20)])
