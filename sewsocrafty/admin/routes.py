from flask import (Blueprint, render_template, url_for,
                   flash, redirect, request)
from flask_login import login_user, logout_user, current_user, login_required
from sewsocrafty import db, bcrypt
from sewsocrafty.forms import LoginForm, RegistrationForm, MyButtonField
from sewsocrafty.models import Admin, Products, Pages


admin = Blueprint('admin', __name__)


### the bulk of the work for the site will likely end up in this file.
### based on this there will be a LOT of routes, and likely a decent amount
### of code in several of them.

# admin
#   - product
#       = edit (product)
#       = add (product)
#       = delete (product)
#   - user
#       = edit (current user)
#       = add (new user)
#       = delete existing user
#   - page
#       = edit dynamic page content



@admin.route("/admin", methods=['GET', 'POST'])
def admin_page():
    # if the user is logged in, show the page
    if current_user.is_authenticated:
        user = current_user.first_name
        return render_template('admin/admin.html', user=user)
    else:
        # otherwise, send them to the login page
         return redirect(url_for('admin.login'))

@admin.route("/admin/reset_request", methods=['GET', 'POST'])
def reset_request():
    # hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    pass

@admin.route("/admin/login", methods=['GET', 'POST'])
def login():
    #if current_user.is_authenticated:
    #   return redirect(url_for('admin.admin_page'))

    ## check to see if a password is set, if not, don't allow logins,
    ## instead point user to email
    title = "Log In to SewSoCrafty"
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            return redirect(url_for('admin.admin_page'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'warning')

    return render_template('admin/login.html', title=title, form=form)

@admin.route("/admin/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@admin.route("/admin/register", methods=['GET', 'POST'])
def register():
    print("Register was run.")
    title = "Register a New Admin"
    form = RegistrationForm()


    if form.validate_on_submit():
        if form.image_file:
            ## don't store user-generated filename!
            ## generate a random 16char string as a filename
            image_file=form.image_file.data
        # no password actions here, email token will be sent below
        admin = Admin(username=form.username.data, first_name=form.first_name.data,
                      last_name=form.last_name.data, email=form.email.data,
                      phone_num=form.phone_num.data, image_file=image_file)
        #db.session.add(admin)
        #db.session.commit()

        ## add email token to newly created user to set up password

        flash(f'Account created for {form.username.data}! \
                Advise {form.first_name.data} {form.last_name.data} \
                to check their email at {form.email.data} \
                to set up a password.', 'success') # check 'success' for bulma
        return redirect(url_for('admin.admin_page'))

    return render_template('admin/register.html', title=title, form=form)



