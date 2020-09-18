from flask import Flask, render_template_string # ButtonWidget
from flask_wtf import FlaskForm, Form # ButtonWidget
from flask_wtf.file import FileField, FileAllowed
from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import html_params, HTMLString # ButtonWidget
# from sewsocrafty.models import User
# from flask_login import current_user


class ButtonWidget(object):
    a_class = 'button is-fullwidth rounded secondary-btn'
    a_id = 'submit'
    a_type = 'submit'
    a_value = 'Log In'
    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class', self.a_class)
        kwargs.setdefault('id', self.a_id)
        kwargs.setdefault('type', self.a_type)
        kwargs.setdefault('value', self.a_value)

        return HTMLString('<input {params}>'.format(
            params=self.html_params(name=field.name, **kwargs),
            label=field.label.text)
            )

class MyButtonField(StringField):
    widget = ButtonWidget()

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # submit = SubmitField('Log In')
    submit = MyButtonField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                            Length(min=2, max=20)])
    # password field will NOT be used, newly created user will
    # get an email token to set their password prior to initial login...
    first_name = StringField('First Name', validators=[DataRequired(),
                              Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(),
                             Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_num = StringField('Phone Number', validators=[DataRequired(),
                             Length(min=10, max=14)])
    picture = FileField('Picture', validators=[FileAllowed(['jpg', 'png', 'gif'])])
    submit = MyButtonField('Create New Admin')

