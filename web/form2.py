from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField, SelectField
from wtforms.fields.html5 import EmailField
import sys
import psycopg2
from flask import request


class FormDelete(Form):
    c_list = StringField('ID', validators=[
        validators.DataRequired(),
    ])
    submit = SubmitField('Sure?')
