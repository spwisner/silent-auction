import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, login_required, logout_user, current_user
from silentauction.models import Auction, AuctionItem, Photo, Bid, User
from silentauction import db
from silentauction.auction_items.views import get_highest_bid, get_top_bid_summary
import stripe

public_key = os.getenv('STRIPE_PUBLIC_KEY')
stripe.api_key = os.getenv('STRIPE_PRIVATE_KEY')

payments_blueprint = Blueprint('payments', __name__,
                               template_folder='templates/payments')

@payments_blueprint.route('/<int:auction_item_id>', methods=['GET', 'POST'])
@login_required
def payment(auction_item_id):
    auction_item = AuctionItem.query.get(auction_item_id)
    bids = Bid.query.filter_by(auction_item_id=auction_item_id)
    highest_bid = None if bids.count() is 0 else get_highest_bid(bids)
    top_bid_summary = None if highest_bid is None else get_top_bid_summary(highest_bid, bids.count())

    # if highest_bid is None or top_bid_summary is None:
    #     return redirect(url_for('auctions_items.view_auction_item', auction_item_id=auction_item_id))

    # if highest_bid.user_id != current_user.id: 
    #     return redirect(url_for('auctions_items.view_auction_item', auction_item_id=auction_item_id))

    return render_template('payment.html', auction_item=auction_item, top_bid_summary=top_bid_summary)

@payments_blueprint.route('/<int:auction_item_id>/received', methods=['GET', 'POST'])
@login_required
def payment_received(auction_item_id):
    bids = Bid.query.filter_by(auction_item_id=auction_item_id)
    highest_bid = None if bids.count() is 0 else get_highest_bid(bids)
    top_bid_summary = None if highest_bid is None else get_top_bid_summary(highest_bid, bids.count())

     # CUSTOMER INFORMATION
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                      source=request.form['stripeToken'])

    # CHARGE/PAYMENT INFORMATION
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=top_bid_summary.amount,
        currency='usd',
        description='Donation'
    )

    return render_template('paymentreceived.html')