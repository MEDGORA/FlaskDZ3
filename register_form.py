from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class Registration(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    second_name = StringField("Фамилия", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("пароль", validators=[DataRequired(), Length(min = 8)])
    confirm_password = PasswordField("пароль", validators=[DataRequired(), EqualTo("password")])