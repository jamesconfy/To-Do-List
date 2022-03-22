from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class ToDoList(FlaskForm):
    todo = TextAreaField('To Do', validators=[DataRequired(), Length(min=1, max=2000000, message='Check Your Message')])
    submit = SubmitField('Submit')