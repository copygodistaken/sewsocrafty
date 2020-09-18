from flask import (Blueprint, render_template, url_for,
                   flash, redirect, request)
from flask_login import login_user, logout_user, current_user, login_required
# from sewsocrafty import db, bcrypt
from sewsocrafty.forms import LoginForm, RegistrationForm, MyButtonField
# from sewsocrafty.mymethods import Admin, Post


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



@admin.route("/admin")
def admin_page():
    # if the user is logged in, show the page
#    if current_user.is_authenticated:
#        return render_template('admin/admin.html')
#    else:
        # otherwise, send them to the login page
        # return redirect(url_for('admin.login'))
    return render_template('admin/admin.html')

@admin.route("/admin/reset_request", methods=['GET', 'POST'])
def reset_request():
    pass

@admin.route("/admin/login", methods=['GET', 'POST'])
def login():
    title = "Log In to SewSoCrafty"
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data, form.password.data)
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('admin.admin_page'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

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
        flash(f'Account created for {form.username.data}! \
                Advise {form.user_first.data} to check their email \
                at {form.email.data} to set up a password.', 'success') # check 'success' for bulma
    return render_template('admin/register.html', title=title, form=form)



