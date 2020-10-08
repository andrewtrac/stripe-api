from flask import Flask, jsonify, request
from flask_cors import CORS
import stripe

stripe.api_key = 'sk_test_51HYxoFFsExQBHc34bCJ9S2nLHBoO4QV90VhJ5Sil58EQAzL1D4HMOI01ti7taoiAubyA0cunR0Aw3shFe0AN1Mh500gEbusnhI'
app = Flask(__name__,
            static_url_path='',
            static_folder='.')
CORS(app)


app.config["DEBUG"] = True

YOUR_DOMAIN = 'http://localhost:3000/'


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Massage Therapy Session',
                            'images': ['https://www.msccollege.edu/wp-content/uploads/2019/05/how-long-to-become-a-massage-therapist.jpg'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + 'rewards',
            cancel_url=YOUR_DOMAIN + 'appointment',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403
if __name__ == '__main__':
    app.run(port=4242)
  