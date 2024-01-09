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
    return render_template('list.html', auctions=auctions)

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

@auctions_blueprint.route('/<int:record_id>')
def view_auction(record_id):
    # Use the record_id in your view logic (e.g., fetch the record from the database)
    # For now, let's just return a simple response
    print(record_id)
    # auction_items = AuctionItem.query.filter_by(auction_id=record_id)
    auction_items = AuctionItem.query.all()

    return render_template('view.html', auction_items=auction_items)
    

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