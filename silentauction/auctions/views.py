from flask import Blueprint, render_template, redirect, url_for
from silentauction.auctions.forms import CreateForm
from silentauction import db
from silentauction.models import Auction, AuctionItem, Photo

auctions_blueprint = Blueprint('auctions', __name__,
                               template_folder='templates/auctions')

@auctions_blueprint.route('/')
def list():
    # Grab a list of auctions from database.
    auctions = Auction.query.all()
    auctions_count = Auction.query.count()

    # auctions = [auctions(obj.auction_start, convert_to_readable_datetime(obj.auction_start)) for obj in auctions]
    # auctions = [auctions(obj.auction_end, convert_to_readable_datetime(obj.auction_end)) for obj in auctions]

    return render_template('list.html', auctions=auctions, auctions_count=auctions_count)


@auctions_blueprint.route('/create', methods=['POST', 'GET'])
def create():
    form = CreateForm()

    if form.validate_on_submit():
        name = form.name.data
        new_auction = Auction(name)
        db.session.add(new_auction)
        db.session.commit()

        return redirect(url_for('auctions.list'))
    
    return render_template('create.html', form=form)

default_auction_photo = {
    "id": -1,
    "filename": "no-image-available.png",
    "caption": ""
}

@auctions_blueprint.route('/<int:auction_id>')
def view_auction(auction_id):
    auction = Auction.query.get(auction_id)
    auction_items = AuctionItem.query.filter_by(auction_id=auction_id)
    auction_item_ids = [item.id for item in auction_items]
    
    auction_photos = []
    for auction_item_id in auction_item_ids:
        photo = Photo.query.filter_by(auction_item_id = auction_item_id).first()
        photo = default_auction_photo if photo is None else photo
        auction_photos = [*auction_photos, photo]

    return render_template('view.html', auction_items=auction_items, auction=auction, auction_photos=auction_photos)