from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField, SelectField
from wtforms.fields.html5 import EmailField
import sys
import psycopg2
from flask import request


class FormDelete(Form):
	c_list = StringField('Cancel your ticket?', validators=[
        validators.DataRequired(),
    ])
	submit = SubmitField('Farewell')
