from flask import current_app as app, render_template, flash, redirect, url_for
from flask_login import current_user, login_required
import stripe
from .models import Cart
from app import db

stripe.api_key = "sk_test_51L7nhTKW2PHafdlZ2JG2Qs0B1s93zhy5dxHQTIIwkl11s1qHWLQgpn4nzIDUeXBuApzW1fq5GBZ0snR8Lj9r9Vl500SDgU5KmF"


@app.route('/items')
def items():
    products = []
    for product in stripe.Product.list()['data']:
        product_dict = {
            'id': product['id'],
            'name': product['name'],
            'description': product['description'] ,
            'price':stripe.Price.retrieve(product['default_price']) ['unit_amount'] /100,
            'image': product['images'][0],
        }
        products.append(product_dict)
    return render_template('shop/items.html', products=products )

@app.route('/checkout')
def checkout():
    return 'Checkout'

@app.route('/add/to/cart/<product_id>')

def add_to_cart(product_id):
    user_cart = Cart.query.filter_by(user_id=current_user.get_id())
    cart_item = user_cart.filter_by(product_id=product_id).first()

    if cart_item is None:
        cart = Cart(product_id=product_id, user_id=current_user.get_id(), quantity=1)
        db.session.add(cart)
        # db.session.commit()


    else:
        cart_item.quantity += 1    
        db.session.commit()

    
    flash('Item Added')
    return redirect(url_for('items'))

@app.route('/cart')
def cart():
    cart_items = []
    for item in Cart.query.filter_by(user_id=current_user.get_id()).all():
        stripe_product = stripe.Product.retrieve(item.product_id)
        price = stripe.Price.retrieve(stripe_product['default_price']) ['unit_amount'] / 100
        product_dict = {
            'info': stripe_product,
            'price': f"{price:,.2f}",
            'quantity': item.quantity
        }
        cart_items.append(product_dict)

    return render_template('/shop/cart.html')