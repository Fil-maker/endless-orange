from flask_wtf import FlaskForm
from wtforms import HiddenField, RadioField
from wtforms.validators import AnyOf, DataRequired


class ThirdWheelSettingsForm(FlaskForm):
    mode = HiddenField(validators=[DataRequired(), AnyOf(["third-wheel"])])
    level = RadioField(choices=[1, 2, 3], validators=[DataRequired()])
