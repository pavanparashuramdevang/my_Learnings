from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    username=StringField('username',
                         validators=[DataRequired(),Length(min=2,max=50)])
    
    email=StringField('email',
                      validators=[DataRequired()])
    
    password=PasswordField('password',validators=[DataRequired()])
    confirm_password=PasswordField('confirm password',
                                   validators=[DataRequired(),EqualTo('password')])
    
    submit=SubmitField('sign up')


class LoginForm(FlaskForm):   
    email=StringField('email',
                      validators=[DataRequired()])
    
    password=PasswordField('password',validators=[DataRequired()])    
    submit=SubmitField('login')
    

    

