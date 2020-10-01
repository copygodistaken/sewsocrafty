from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask_mail import Mail
from .config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.login_message_category = 'info'

# mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    if app.config == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    # mail.init_app(app)

    from sewsocrafty.admin.routes import admin
    from sewsocrafty.products.routes import products
    from sewsocrafty.main.routes import main
    from sewsocrafty.errors.handlers import errors
    app.register_blueprint(admin)
    app.register_blueprint(products)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
