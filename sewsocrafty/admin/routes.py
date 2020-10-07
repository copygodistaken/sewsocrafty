from flask import (Blueprint, render_template, url_for,
                   flash, redirect, request)
from flask_login import login_user, logout_user, current_user, login_required
from sewsocrafty import db, bcrypt
from sewsocrafty.forms import LoginForm, RegistrationForm, MyButtonField, UpdateAdminForm
from sewsocrafty.models import Admin, Products, Pages
from sewsocrafty.admin.utilities import save_picture


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
    pass

@admin.route("/admin/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
       return redirect(url_for('admin.admin_page'))

    ## check to see if a password is set, if not, don't allow logins,
    ## instead point user to email
    title = "Log In to SewSoCrafty"
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.admin_page'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'warning')

    return render_template('admin/login.html', title=title, form=form)

@admin.route("/admin/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@admin.route("/admin/register", methods=['GET', 'POST'])
@login_required
def register():
    title = "Register a New Admin"
    form = RegistrationForm()

    if form.validate_on_submit():
        if form.image_file.data:
            ## don't store user-generated filename!
            ## generate a random 16char string as a filename
            empty = default.png
            image_file = save_picture(form.image_file.data, empty)
        # no password actions here, email token will be sent below
        admin = Admin(username=form.username.data, first_name=form.first_name.data,
                      last_name=form.last_name.data, email=form.email.data,
                      phone_num=form.phone_num.data, image_file=image_file)
        db.session.add(admin)
        db.session.commit()

        ## add email token to newly created user to set up password

        flash(f'Account created for {form.username.data}! \
                Advise {form.first_name.data} {form.last_name.data} \
                to check their email at {form.email.data} \
                to set up a password.', 'success') # check 'success' for bulma
        return redirect(url_for('admin.admin_page'))

    return render_template('admin/register.html', title=title, form=form)

def check_user(id, un, em, ph, list):
    ### checks to ensure username/email/phone are not already taken by a *different* user
    for person in list:
        if id != person.id:
            if un == person.username:
                flash(f"'{un}' is taken by user {person.id}!", "danger")
                return redirect(url_for('admin.account', username=un))
            if em == person.email:
                flash(f"'{em}' is taken by user {person.id}!", "danger")
                return redirect(url_for('admin.account', username=un))
            if ph == person.phone_num:
                flash(f"'{ph}' is user {person.id}'s phone number!", "danger")
                return redirect(url_for('admin.account', username=un))


@admin.route("/admin/account/<string:username>", methods=['GET', 'POST'])
@login_required
# landing page for when clicking on "who edited this last/created this"
# should check to see if this is the user listed and allow edits if so

def account(username):
    form = UpdateAdminForm()
    title = "Update Admin Information"
    admin = Admin.query.filter_by(username=username).first_or_404()
    admin_list = Admin.query.order_by(Admin.last_name)
    image = url_for('static', filename='images/admins/' + admin.image_file)
    if form.validate_on_submit():
        if form.image_file.data:
            admin.image_file = save_picture(form.image_file.data, admin.image_file)
        check_user(admin.id, admin.username, admin.email, admin.phone_num, admin_list)
        admin.username = form.username.data
        admin.first_name = form.first_name.data
        admin.last_name = form.last_name.data
        admin.email = form.email.data
        admin.phone_num = form.phone_num.data
        if form.is_su_checked.data:
            admin.is_su = form.is_su_checked.data
        else:
            admin.is_su = form.is_su_unchecked.data
        db.session.commit()

        flash(f"{form.username.data}'s account information has been updated!", 'success')
        return redirect(url_for('admin.account', username=admin.username))
    elif admin.username == current_user.username or current_user.is_su:
        return render_template('admin/edit_admin.html', form=form, title=title, admin=admin, admin_list=admin_list)


    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('admin/account.html', title='Account', \
                            form=form, admin=admin, admin_list=admin_list)



