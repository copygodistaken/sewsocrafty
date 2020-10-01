from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as TimedJSONWebSignatureSerializer
from . import db, login_manager
from flask_login import UserMixin
from flask import current_app


@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))
    return Admin.get(admin_id)



# each class becomes its own table in the DB
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60)) ## must be nullable to allow email token for initial password
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_num = db.Column(db.String(10), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    # places that link to the admin table using admin.id
    # products = db.relationship('Products', backref='author', lazy=True)
    prod_auth = db.relationship("Products", backref='author', lazy=True)
    page_auth = db.relationship("Pages", backref='author', lazy=True)
    prod_edit = db.relationship("Product_Edits", backref='editor', lazy=True)
    page_edit = db.relationship("Page_Edits", backref='editor', lazy=True)

    def __repr__(self):
        return f"Admin('{self.username}', '{self.email}', '{self.image_file}')"


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String(100), nullable=False)
    prod_desc = db.Column(db.Text, nullable=False)
    prod_price = db.Column(db.String(7))
    prod_cost = db.Column(db.String(7), nullable=False)
    prod_labor = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    tags = db.Column(db.String(100))
    # create local path for product images, then use hashes to store filenames
    image1 = db.Column(db.String(20))
    image2 = db.Column(db.String(20))
    image3 = db.Column(db.String(20))
    image4 = db.Column(db.String(20))
    image5 = db.Column(db.String(20))
    # links to Admin.prod_auth
    author_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    # anchor for Product_Edits.prod_id
    edits = db.relationship("Product_Edits", )

    def __repr__(self):
        return f"Products('{self.prod_name}', '{self.prod_price}', '{self.image1}', '{self.date_added}')"


# Product_Edits (for now) will only track WHO edited products, not WHAT was edited
class Product_Edits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # link to Admin.prod_edit (admin.id)
    edit_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    # link to Products.edits (products.id)
    prod_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)


class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    text1 = db.Column(db.String(200), nullable=True)
    text2 = db.Column(db.String(200), nullable=True)
    text3 = db.Column(db.String(200), nullable=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime)
    # link to Admin.page_auth (admin.id)
    author_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    # anchor for Page_Edits.page_id
    edits = db.relationship("Page_Edits")

    def __repr__(self):
        return f"Pages('{self.title}', '{self.text1}')"


class Page_Edits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # link to Admin.page_edit (admin.id)
    edit_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    # link to Pages.edits (pages.id)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'), nullable=False)


admin_1 = Admin(username='eric', email='eric@33ad.org', password='password')
