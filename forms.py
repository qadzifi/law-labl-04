from flask_wtf import FlaskForm
from wtforms import TextAreaField

class Base64InputForm(FlaskForm):
    input_string = TextAreaField('Sample text')
