from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Sign Up')
    
class SigninForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Sign In')
    

class PostForm(FlaskForm):
    body = StringField('Input you car information', validators=[DataRequired()])
    submit = SubmitField('Publish')
    
    
class CommentForm(FlaskForm):
    body = StringField("Input car's information you like to add to my collection", validators=[DataRequired()])
    submit = SubmitField('Publish')