import os


class Config(object):
    DEBUG = False
    TESTING = False
    # add to .bash_profile as exports (export ABC=123)
    # to enable on server, then change to
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = "fyZD2w7XlupqbqNIWFiTSEBvgOMr3DS"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # update this stuff to enable password reset emails
    # (or any emails for that matter)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # add EMAIL_USER and EMAIL_PASS to environment variables to
    # set up appropriate email info
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
