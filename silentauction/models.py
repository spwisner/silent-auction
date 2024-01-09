from silentauction import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id): 
    return User.query.get(user_id)

class User (db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    # created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"User has email {self.email}"
    
class Auction (db.Model):
    __tablename__ = "auctions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    auction_items = db.relationship('AuctionItem',backref='auction',lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Auction name is {self.name}"
    
    def report_auction_items(self):
        print("Here are the auction items:")
        for auction_item in self.auction_items:
            print(auction_item.name)

class AuctionItem(db.Model):
    __tablename__ = 'auction_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    auction_id = db.Column(db.Integer,db.ForeignKey('auctions.id'), nullable=False)
    # created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # auction = db.relationship('Auction', backref='auction', uselist=False) # uselist = False because 1 to 1 and not 1 to many
    # 1 to many
    # bids = db.relationship('Bid', backref='auctionItem', lazy='dynamic') #lazy describes how items should be loaded
    # 1 to 1
    # owner = db.relationship('Owner', backref='itemOwner', uselist=False) # uselist = False because 1 to 1 and not 1 to many

    def __init__(self, name, auction_id):
        self.name = name
        self.auction_id = auction_id
        # self.created_at = created_at
        # self.updated_at = updated_at

    def __repr__(self):
        return f"Auction item is {self.name}"
    


class Bid(db.Model):
    __tablename__ = "bids"
    id = db.Column(db.Integer, primary_key=True)
    # created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, name):
        self.name = name
        # self.created_at = created_at
        # self.updated_at = updated_at

    def __repr__(self):
        return f"Bid has id {self.id}"

# db.create_all()