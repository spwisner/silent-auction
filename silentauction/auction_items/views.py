from flask import Blueprint, render_template, redirect, url_for, request, flash
from silentauction import db
from silentauction.models import Auction, AuctionItem, Photo, Bid, User
from datetime import datetime
from flask_login import current_user

auction_items_blueprint = Blueprint('auction_items', __name__,
                               template_folder='templates/auction_items')

def get_highest_bid(bids):
    return sorted(bids, key=lambda x: x.amount, reverse=True)[0]

def get_next_bid_amount(highest_bid, auction_item):
    highest_bid_amount = None if (highest_bid is None) else highest_bid.amount
    next_bid_amount = auction_item.starting_bid if (highest_bid_amount is None or highest_bid_amount < auction_item.starting_bid) else (highest_bid_amount + auction_item.bid_interval)
    return next_bid_amount

def get_top_bid_summary(highest_bid, bids_count):
    top_bid_user = User.query.get(highest_bid.user_id)
    return {
        'amount': highest_bid.amount,
        'user_id': top_bid_user.id,
        'username': top_bid_user.username,
        'bids_count': bids_count
    }

@auction_items_blueprint.route('/<int:auction_item_id>', methods=['GET', 'POST'])
def view_auction_item(auction_item_id):
    auction_item = AuctionItem.query.get(auction_item_id)
    bids = Bid.query.filter_by(auction_item_id=auction_item_id)
    highest_bid = None if bids.count() is 0 else get_highest_bid(bids)
    auction = Auction.query.get(auction_item.auction_id)
    next_bid_amount = get_next_bid_amount(highest_bid=highest_bid, auction_item=auction_item)
    current_time = datetime.utcnow()
    has_auction_started = current_time >= auction_item.auction_start
    has_auction_ended = current_time >= auction_item.auction_end
    is_auction_item_active = auction_item.auction_start <= current_time < auction_item.auction_end

    top_bid_summary = None if highest_bid is None else get_top_bid_summary(highest_bid, bids.count())

    auction_item_photos = Photo.query.filter_by(auction_item_id=auction_item.id)
    return render_template('view_auction_item.html', 
                           auction_item=auction_item, 
                           auction_item_photos=auction_item_photos, 
                           next_bid=next_bid_amount, 
                           has_auction_started=has_auction_started,
                           has_auction_ended=has_auction_ended,
                           is_auction_item_active=is_auction_item_active,
                           auction=auction,
                           top_bid_summary=top_bid_summary
                           )

@auction_items_blueprint.route('/<int:auction_item_id>/bid', methods=['GET', 'POST'])
def bid_on_auction_item(auction_item_id):
    auction_item = AuctionItem.query.get(auction_item_id)
    highest_bid = Bid.query.filter_by(auction_item_id=auction_item.id).order_by(Bid.amount.desc()).first()
    next_bid_amount = get_next_bid_amount(highest_bid=highest_bid, auction_item=auction_item)
    next_bid_as_float = round(float(next_bid_amount), 2)

    hidden_auction_item_id = request.args.get('hidden_auction_item_id')
    if int(hidden_auction_item_id) != auction_item.id:
        raise ValueError("The auction item id does not match the bid auction item id.")
    
    hidden_bid_amount = round(float(request.args.get('hidden_bid_amount')), 2)
    
    hidden_user_id = request.args.get('hidden_user_id')
    if int(hidden_user_id) != current_user.id:
        raise ValueError("The user registered in the UI does not match the current user")

    current_time = datetime.utcnow()

    if hidden_auction_item_id and hidden_bid_amount and hidden_user_id:
        if current_time >= auction_item.auction_end:
            flash(f"Error: Bid received after auction ended.")
            return redirect(url_for('auction_items.view_auction_item', auction_item_id=auction_item.id))
        elif round(float(hidden_bid_amount), 2) != next_bid_as_float:
            flash(f"The bid you placed is no longer the highest bid.")
            return redirect(url_for('auction_items.view_auction_item', auction_item_id=auction_item.id))
        else:
            bid = Bid(amount=next_bid_amount, auction_item_id=auction_item_id, user_id=current_user.id)
            db.session.add(bid)
            db.session.commit()
            flash(f"Your bid of ${next_bid_amount} was successful.")
            return redirect(url_for('auction_items.view_auction_item', auction_item_id=auction_item.id))
    
    raise ValueError("An unexpected error occurred")

