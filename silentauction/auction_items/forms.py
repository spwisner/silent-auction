from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from silentauction.models import User

class BidForm(FlaskForm):
    hidden_auction_item_id = HiddenField()
    hidden_bid_amount = HiddenField()
    hidden_user_id = HiddenField()
    submit = SubmitField('Bid')