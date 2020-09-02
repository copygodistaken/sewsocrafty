from flask import Flask


app = Flask(__name__)
if app.config == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

from app import routes

