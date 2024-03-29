from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, login_required, logout_user, current_user
from silentauction import db
from silentauction.models import User, AuctionItem, Bid
from silentauction.users.forms import LoginForm, RegistrationForm
from datetime import datetime

users_blueprint = Blueprint('users', __name__,
                            template_folder='templates/users')

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!')

            next = request.args.get('next')

            if (next == None or not next[0]== '/'):
                next = url_for('auctions.list')
            return redirect(next)
        else:
            flash('Login failed.  Please try again.')
        
    return render_template('login.html', form=form)

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    username=form.username.data,
                    password=form.password.data
                    )
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Successfully logged out.")
    return redirect(url_for('index'))

@users_blueprint.route('/settings/user-profile')
@login_required
def settings_user_profile():
    return render_template('settings_user_profile.html')


@users_blueprint.route('/settings/items-won')
@login_required
def items_won():
    current_time = datetime.utcnow()

    auction_items = AuctionItem.query.filter(AuctionItem.auction_end < current_time).all()

    items_won = []
    for auction_item in auction_items:
        highest_bid = Bid.query.filter_by(auction_item_id=auction_item.id).order_by(Bid.amount.desc()).first()
        if highest_bid is not None:
            highest_bid_user_id = highest_bid.user_id
            if highest_bid_user_id == current_user.id:
                items_won = [*items_won, auction_item]

    return render_template('items_won.html', items_won=items_won)
