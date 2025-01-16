from flask_wtf import FlaskForm

from wtforms import FloatField, StringField, PasswordField, SubmitField, IntegerField, RadioField, BooleanField, TextAreaField, SelectField, ValidationError, FieldList, FormField
from wtforms.validators import DataRequired, EqualTo, Email, Optional, Length, NumberRange

from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

from app import db
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match.")])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Register')
#NEED TO VALIDATE THAT EMAIL IS APART OF LEADERSHIP TEAM AND EACH EMAIL MUST BE UNIQUE