from flask import Flask, render_template_string # ButtonWidget
from flask_wtf import FlaskForm, Form # ButtonWidget
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField, HiddenField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import html_params, HTMLString # ButtonWidget
from .models import Admin
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
    is_su = BooleanField('Ability to add and remove other Admins?')
    submit = MyButtonField('Create Admin')

    def validate_username(self, username):
        # check submitted username against the usernames in the database
        if username.data != current_user.username:
            admin = Admin.query.filter_by(username=username.data).first()
            if admin:
                raise ValidationError('{admin.username} is taken! Please choose a different user name!')

    def validate_email(self, email):
        # check submitted username against the emails in the database
        if email.data != current_user.email:
            admin = Admin.query.filter_by(email=email.data).first()
            if admin:
                raise ValidationError(admin.email + ' is taken! Please choose a different email!')

    def validate_phone_num(self, phone_num):
        # ensure two people aren't using the same phone number
        admin = Admin.query.filter_by(phone_num=phone_num.data).first()
        if admin:
            raise ValidationError(admin.phone_num + ' is taken! Please choose a different phone number!')

class UpdateAdminForm(FlaskForm):
    admin_id = HiddenField('admin_id')
    username = StringField('Username', validators=[InputRequired(),
                            Length(min=2, max=20)])
    first_name = StringField('First Name', validators=[InputRequired(),
                            Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[InputRequired(),
                            Length(min=2, max=30)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    phone_num = StringField('Phone Number', validators=[InputRequired(),
                             Length(min=10, max=14)])
    image_file = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'gif'])])
    is_su_checked = BooleanField('Ability to add and remove Admins?', default='checked')
    is_su_unchecked = BooleanField('Ability to add and remove Admins?')
    #is_su = SelectField('Ability to add and remove Admins?', choices=[(True, 'Yes'), (False, 'No')])
    ## passwords handled by ResetPasswordForm() to ensure SUs don't change
    ## user passwords without the users (must be mailed to email address)
    submit = MyButtonField('Update Admin')


    ##### Validations MUST occur in the python routes due to the requirement
    ##### to check against the database to ensure the allowance of "duplicate"
    ##### usernames/emails as long as the admin_id remains the same...
    #def validate_username(self, username, admin_id):
    #    admin_list = Admin.query.order_by(Admin.id)
    #    for admin in admin_list:
    #        print(admin.username, " - ", current_user.username, " - ", current_user.is_su)
    #        if admin.username == username & admin.id != admin_id:
    #            raise ValidationError('That username is taken! Please choose a different one!')

    # def validate_email(self, email):
    #     if email.data != current_user.email:
    #         # check submitted email against the emails in the database
    #         admin = Admin.query.filter_by(email=email.data).first()
    #         if admin:
    #             raise ValidationError('That email is taken! Please choose a different one!')


