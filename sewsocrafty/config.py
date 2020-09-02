import os


class Config:
    # add to .bash_profile as exports (export ABC=123)
    # to enable on server, then change to
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = "EzHjXVkZttmDfplQLgZ4Ed1GnA.8PPO"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # update this stuff to enable password reset emails
    # (or any emails for that matter)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # add EMAIL_USER and EMAIL_PASS to environment variables to
    # set up appropriate email info
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
