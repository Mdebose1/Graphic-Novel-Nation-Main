from flask import current_app as app
from flask_login import current_user
import stripe
from app.blueprints.shop.models import Cart

@app.context_processor
def cart_context():
        cart_dict = {}
        if current_user.is_anonymous:
                return {
                'cart_items': cart_dict,
                'cart_quantity': 0,
                'cart_subtotal': 0,
                'cart_grandtotal': 0,

                }

        cart1 = Cart.query.filter_by(user_id=current_user.get_id()).all()
        if len(cart1) > 0:
                for item in cart1:
                        stripe_product = stripe.Product.retrieve(item.product_id)
                        if item not in cart_dict:
                                cart_dict[stripe_product['id']] = {
                                        'id': item.id ,
                                        'product_id': stripe_product['id'],
                                        'image':stripe_product['images'][0] ,
                                        'quantity': 1,
                                        'description': stripe_product['description'],
                                        'price': stripe.Price.retrieve(stripe_product['default_price'])['unit_amount']
                                }
        else:
                cart_dict[stripe_product['id']]['quantity'] += 1
        grandtotal = sum([product['price'] * product['quantity'] for product in cart_dict.values()]) / 100
        return  {
'cart_items': cart_dict,
'cart_quantity': sum([product.quantity for product in cart1]),
'cart_subtotal': 0,
'cart_grandtotal': f'{grandtotal:,.2f}',

}



