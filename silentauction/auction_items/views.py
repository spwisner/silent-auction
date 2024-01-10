from flask import Blueprint, render_template, redirect, url_for
from silentauction import db
from silentauction.models import Auction, AuctionItem

auction_items_blueprint = Blueprint('auction_items', __name__,
                               template_folder='templates/auction_items')

@auction_items_blueprint.route('/<int:auction_item_id>')
def view_auction_item(auction_item_id):
    # Grab a list of auctions from database.
    auction_item = AuctionItem.query.get(auction_item_id)
    return render_template('view_auction_item.html', auction_item=auction_item)

