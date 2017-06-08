from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class TransmogrificationForm(FlaskForm):
    data_to_transmogrify_field = TextAreaField('transmogrify_field_label',validators=[DataRequired()])

