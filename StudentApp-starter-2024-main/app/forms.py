from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  Length

class CourseForm(FlaskForm):
    coursenum = StringField('Course Number',[Length(min=3, max=6)])
    submit = SubmitField('Post')
