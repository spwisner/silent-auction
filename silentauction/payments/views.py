import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from silentauction.models import Auction, AuctionItem, Photo, Bid, User
from silentauction import db, app
from silentauction.auction_items.views import get_highest_bid, get_top_bid_summary
import stripe

public_key = os.getenv('STRIPE_PUBLIC_KEY')
stripe.api_key = os.getenv('STRIPE_PRIVATE_KEY')
domain = os.getenv('DOMAIN')

IS_DEMO = os.getenv('IS_DEMO') == 'true'

payments_blueprint = Blueprint('payments', __name__,
                               template_folder='templates/payments')

@payments_blueprint.route('/<int:auction_item_id>', methods=['GET', 'POST'])
@login_required
def payment(auction_item_id):
    auction_item = AuctionItem.query.get(auction_item_id)

    bids = Bid.query.filter_by(auction_item_id=auction_item_id)
    highest_bid = None if bids.count() is 0 else get_highest_bid(bids)
    top_bid_summary = None if highest_bid is None else get_top_bid_summary(highest_bid, bids.count())

    if highest_bid is None or top_bid_summary is None:
        return redirect(url_for('auction_items.view_auction_item', auction_item_id=auction_item_id))

    if highest_bid.user_id != current_user.id: 
        return redirect(url_for('auction_items.view_auction_item', auction_item_id=auction_item_id))

    if auction_item.has_paid:
        return render_template('already-paid.html')

    if IS_DEMO == True:
        flash('To demo payments, use the card number 4242 4242 4242 4242 with any future expiration date and any CVC number.', 'info')
    
    return render_template('payment.html', auction_item=auction_item, top_bid_summary=top_bid_summary)

@payments_blueprint.route('/create-checkout-session/<int:auction_item_id>', methods=['POST'])
@login_required
def create_checkout_session(auction_item_id):
    auction_item = AuctionItem.query.get(auction_item_id)
    if (auction_item is None):
        raise ValueError('No auction item found')

    bids = Bid.query.filter_by(auction_item_id=auction_item_id)
    highest_bid = None if bids.count() is 0 else get_highest_bid(bids)
    
    if (highest_bid is None):
        raise ValueError('No highest bid found')


    price_of_product = stripe.Price.create(
        unit_amount=int(highest_bid.amount * 100),
        currency="usd",
        product=auction_item.stripe_product_id,
    )

    return_url_base = domain + url_for('payments.payment_success', auction_item_id=auction_item_id)

    try:
        session = stripe.checkout.Session.create(
            ui_mode = 'embedded',
            line_items=[
                {
                    'price': price_of_product['id'],
                    'quantity': 1,
                },
            ],
            mode='payment',
            
            return_url= return_url_base + '?session_id={CHECKOUT_SESSION_ID}',
        )
    except Exception as e:
        return str(e)

    return jsonify(clientSecret=session.client_secret)

@payments_blueprint.route('/payment-success/<int:auction_item_id>')
@login_required
def payment_success(auction_item_id):

    session = stripe.checkout.Session.retrieve(request.args.get('session_id'))

    if session.payment_status == 'paid':
        auction_item = AuctionItem.query.get(auction_item_id)
        auction_item.has_paid = True
        db.session.commit()

    return render_template('payment-success.html', auction_item_id=auction_item_id)

@payments_blueprint.route('/session-status', methods=['GET'])
@login_required
def session_status():
  session = stripe.checkout.Session.retrieve(request.args.get('session_id'))

  return jsonify(status=session.status, customer_email=session.customer_details.email)