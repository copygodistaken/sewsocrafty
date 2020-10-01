from flask import Flask, render_template_string # ButtonWidget
from flask_wtf import FlaskForm, Form # ButtonWidget
from flask_wtf.file import FileField, FileAllowed
from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import html_params, HTMLString # ButtonWidget
from sewsocrafty.models import Admin
# from flask_login import current_user


class ButtonWidget(object):
    a_class = 'button is-fullwidth rounded secondary-btn'
    a_id = 'submit'
    a_type = 'submit'
    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class', self.a_class)
        kwargs.setdefault('id', self.a_id)
        kwargs.setdefault('type', self.a_type)

        return HTMLString('<input {params}>'.format(
            params=self.html_params(name=field.name, **kwargs, value=field.label.text)
            ))

class MyButtonField(StringField):
    widget = ButtonWidget()

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    # submit = SubmitField('Log In')
    submit = MyButtonField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),
                            Length(min=2, max=20)])
    # password field will NOT be used, newly created user will
    # get an email token to set their password prior to initial login...
    first_name = StringField('First Name', validators=[InputRequired(),
                            Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[InputRequired(),
                            Length(min=2, max=30)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    phone_num = StringField('Phone Number', validators=[InputRequired(),
                             Length(min=10, max=14)])
    image_file = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'gif'])])
    submit = MyButtonField('Create Admin')

    def validate_username(self, username):
        # check submitted username against the usernames in the database
        admin = Admin.query.filter_by(username=username.data).first
        if admin:
            raise ValidationError('That username is taken! Please choose a different one!')

    def validate_email(self, email):
        # check submitted username against the emails in the database
        admin = Admin.query.filter_by(email=email.data).first
        if admin:
            raise ValidationError('That email is taken! Please choose a different one!')


