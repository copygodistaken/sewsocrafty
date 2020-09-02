from app import app
from flask import request, redirect, render_template

@app.route("/")
def index():
    title = "Home"
    return render_template("home.html", title=title)

@app.route("/reviews")
def reviews():
    pass

@app.route("/admin/login")
def login():
    pass

@app.route("/products")
def products():
    pass

