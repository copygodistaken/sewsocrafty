from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as TimedJSONWebSignatureSerializer
from sewsocrafty import db, login_manager
from flask_login import UserMixin
from flask import current_app


# @login_manager.user_loader
# def load_user(user_id):
#    return User.query.get(int(user_id))
#    return User.get(user_id)

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_num = db.Column(db.String(12), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # not sure user_edits will work like this, we'll look at it in the future...
    user_edits = db.relationship('Edits', backref='author', lazy=True)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String(100), nullable=False)
    prod_desc = db.Column(db.Text, nullable=False)
    prod_price = db.Column(db.String(7))
    prod_cost = db.Column(db.String(7), nullable=False)
    prod_labor = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime)
    tags = db.Column(db.String(100))
    image1 = db.Column(db.String(20))
    image2 = db.Column(db.String(20))
    image3 = db.Column(db.String(20))
    image4 = db.Column(db.String(20))
    image5 = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)




