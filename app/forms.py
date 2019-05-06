from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length

class PostForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), Length(min=1, max=40)])
    email = StringField('Email address', validators=[
        DataRequired(), Length(min=1, max=50)])
    phone = StringField('Phone number', validators=[
        Length(min=1, max=20)])
    reason = StringField('Comment', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')
