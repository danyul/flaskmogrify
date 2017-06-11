from flask_wtf import FlaskForm
from wtforms import TextAreaField, RadioField
from wtforms.validators import DataRequired

class TransmogrificationForm(FlaskForm):

    data_to_transmogrify_field = TextAreaField(
        label='transmogrify_field_label',
        validators=[DataRequired()]
    )

    radio_choices = RadioField(
            label='function_radios',
            choices=["X","Y","Z"]
    )