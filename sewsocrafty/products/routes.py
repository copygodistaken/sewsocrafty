from flask import Blueprint, render_template, request


# producto = Blueprint('products', __name__, template_folder='templates', static_folder='static')
# this (producto) is what's being registered as a blueprint in __init__.py
producto = Blueprint('products', __name__)

# this is adding routes and methods to producto (hence @ decorator?)


@producto.route("/products")
@producto.route("/products/all", methods=['GET', 'POST'])
def all_products():
    # create search function
    return render_template('products.html')


@producto.route("/products/<string:prod>", methods=['GET', 'POST'])
def product_name(prod):
    product = prod
    # utilize search function
    return render_template('products.html', prod=product)

