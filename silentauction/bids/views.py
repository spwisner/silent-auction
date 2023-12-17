from flask import Blueprint, render_template, redirect, url_for, flash, session
from silentauction import db
from silentauction.models import Bid
from silentauction.bids.forms import AddForm

bids_blueprint = Blueprint('bids', __name__,                          
                            template_folder='templates/bids')

@bids_blueprint.route('/bid-successful', methods=['GET', 'POST'])
def bid_successful():
    return render_template('bid-success.html')

@bids_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    bid = False
    is_max_bid = False
    alerts = False
    interest = False
    feedback = False

    form = AddForm()

    if form.validate_on_submit():
        session['bid'] = form.bid.data
        session['is_max_bid'] = form.is_max_bid.data
        session['alerts'] = form.alerts.data
        session['interest'] = form.interest.data
        session['feedback'] = form.feedback.data

        flash('You just clicked the button')

        return redirect(url_for('bids.bid_successful'))

    return render_template('add.html', form=form)



