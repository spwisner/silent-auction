from flask import Blueprint, render_template, redirect, url_for
from silentauction.auctions.forms import CreateForm
from silentauction import db
from silentauction.models import Auction, AuctionItem

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

@auctions_blueprint.route('/<int:auction_id>')
def view_auction(auction_id):
    # Use the record_id in your view logic (e.g., fetch the record from the database)
    # For now, let's just return a simple response

    auction = Auction.query.get(auction_id)
    auction_items = AuctionItem.query.filter_by(auction_id=auction_id)
    print(type(auction_items))
    return render_template('view.html', auction_items=auction_items, auction=auction)
    

# def add():
#     form = AddForm()

#     if form.validate_on_submit():
#         name = form.name.data

#         # Add new Puppy to database
#         new_pup = Puppy(name)
#         db.session.add(new_pup)
#         db.session.commit()

#         return redirect(url_for('puppies.list'))

#     return render_template('add.html',form=form)