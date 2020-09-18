from flask import Blueprint, render_template, request


# producto = Blueprint('products', __name__, template_folder='templates', static_folder='static')
# this (producto) is what's being registered as a blueprint in __init__.py
products = Blueprint('products', __name__)

# this is adding routes and methods to producto (hence @ decorator?)


@products.route("/products")
@products.route("/products/all", methods=['GET', 'POST'])
def all_products():
    css_class = 'hero is-fullheight is-default is-bold'
    product = "Products"
    # create search function
    return render_template('products.html', prod=product, css_class=css_class)


@products.route("/products/<string:prod>", methods=['GET', 'POST'])
def product_name(prod):
    if prod == "Dolldress":
        product = "Doll Dresses"
    else:
        product = prod
    css_class = 'hero is-fullheight is-default is-bold'
    # utilize search function
    return render_template('products.html', prod=product, css_class=css_class)

