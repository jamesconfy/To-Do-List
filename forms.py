from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError

class ToDoList(FlaskForm):
    todo = TextAreaField('To Do', validators=[DataRequired(), Length(min=1, max=2000000, message='Check Your Message')])
    submit = SubmitField('Submit')