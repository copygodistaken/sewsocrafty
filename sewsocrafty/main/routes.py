from flask import Blueprint, render_template, request
# from sewsocrafty.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # title = "Welcome to SewSoCrafty!"
    # just show the home.html data... we'll need to update this to add products
    # once that process is created.
    return render_template('home.html')

@main.route("/about")
def about():
    # pull this data from the database so it can be edited/updated easily
    text1 = "This is information about this website organization."
    text2 = "This is more information about this website organization."
    return render_template('about.html', text1=text1, text2=text2)

@main.route("/reviews")
def reviews():
    pass

# add this to admin/routes.py
@main.route("/admin/login")
def login():
    pass

