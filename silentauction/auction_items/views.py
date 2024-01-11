from flask import Blueprint, render_template, redirect, url_for, request, flash
from silentauction import db
from silentauction.models import Auction, AuctionItem, Photo, Bid
from silentauction.auction_items.forms import BidForm
from datetime import datetime

auction_items_blueprint = Blueprint('auction_items', __name__,
                               template_folder='templates/auction_items')

@auction_items_blueprint.route('/<int:auction_item_id>', methods=['GET', 'POST'])
def view_auction_item(auction_item_id):
    auction_item = AuctionItem.query.get(auction_item_id)
    highest_bid = Bid.query.filter_by(auction_item_id=auction_item.id).order_by(Bid.amount.desc()).first()
    highest_bid_amount = None if (highest_bid is None) else highest_bid.amount
    print(highest_bid_amount)
    next_bid_amount = auction_item.starting_bid if (highest_bid_amount is None or highest_bid_amount < auction_item.starting_bid) else (highest_bid_amount + auction_item.bid_interval)

    current_time = datetime.utcnow()
    # is_auction_item_active = auction_item.auction_start < current_time < auction_item.auction_end
    has_auction_started = current_time > auction_item.auction_start
    has_auction_ended = current_time > auction_item.auction_end
    is_auction_item_active = has_auction_started and not has_auction_ended

    auction_item_photos = Photo.query.filter_by(auction_item_id=auction_item.id)
    return render_template('view_auction_item.html', 
                           auction_item=auction_item, 
                           auction_item_photos=auction_item_photos, 
                           next_bid=next_bid_amount, 
                           has_auction_started=has_auction_started,
                           has_auction_ended=has_auction_ended,
                           is_auction_item_active=is_auction_item_active,
                           )

@auction_items_blueprint.route('/<int:auction_item_id>/bid', methods=['GET', 'POST'])
def bid_on_auction_item(auction_item_id):
    auction_item = AuctionItem.query.get(auction_item_id)
    highest_bid = Bid.query.filter_by(auction_item_id=auction_item.id).order_by(Bid.amount.desc()).first()
    highest_bid_amount = None if (highest_bid is None) else highest_bid.amount
    print(highest_bid_amount)
    next_bid_amount = auction_item.starting_bid if (highest_bid_amount is None or highest_bid_amount < auction_item.starting_bid) else (highest_bid_amount + auction_item.bid_interval)


    #@TODO add validations
    
    hidden_auction_item_id = request.args.get('hidden_auction_item_id')
    hidden_bid_amount = request.args.get('hidden_bid_amount')
    hidden_user_id = request.args.get('hidden_auction_item_id')
    
    if hidden_auction_item_id and hidden_bid_amount and hidden_user_id:
        print("WORKING")
        print(hidden_auction_item_id)
        print(hidden_bid_amount)
        print(hidden_user_id)

        bid = Bid(amount=next_bid_amount, auction_item_id=int(hidden_auction_item_id), user_id=int(hidden_user_id))
        db.session.add(bid)
        db.session.commit()
        print(bid.id)
        # db.session.add(user)
        # db.session.commit()
        flash('Thank you for bidding')
        redirect(url_for('auction_items.view_auction_item', auction_item_id=auction_item.id))
    
        auction_item = AuctionItem.query.get(auction_item_id)
    
        return redirect(url_for('auction_items.view_auction_item', auction_item_id=auction_item.id))
    
    raise ValueError("Invalid")

