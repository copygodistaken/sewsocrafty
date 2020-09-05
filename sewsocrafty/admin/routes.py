from flask import (Blueprint, render_template, url_for,
                   flash, redirect, request)
from flask_login import login_user, logout_user, current_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post


admin = Blueprint('main', __name__)


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
def admin():
    # if the user isn't logged in, give them a 403 error

    # more stuff goes here.
    return render_template('admin.html')

@admin.route("reset_request")
def reset_request():
    pass



@admin.route("/admin/login")
def login():
    pass

@admin.route("/admin/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))




