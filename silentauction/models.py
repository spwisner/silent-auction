from silentauction import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from silentauction.utils.date_utils import default_auction_end, convert_to_readable_datetime, now_plus_days_datetime

@login_manager.user_loader
def load_user(user_id): 
    return User.query.get(user_id)

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(75), nullable=False)
    caption = db.Column(db.String(100))
    category = db.Column(db.String(75), nullable=False)
    subcategory = db.Column(db.String(75), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Foreign Keys
    auction_id = db.Column(db.Integer,db.ForeignKey('auctions.id'))
    auction_item_id = db.Column(db.Integer,db.ForeignKey('auction_items.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __init__(self, filename, category, subcategory, caption=None, auction_id=None, auction_item_id=None, user_id=None, created_at=None, updated_at=None):
        self.filename = filename
        self.caption = caption
        self.category = self.photo_category(category)
        self.subcategory = self.photo_subcategory(category, subcategory)
        self.auction_id = auction_id
        self.auction_item_id = auction_item_id
        self.user_id = user_id
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def photo_category(self, categoryName):
        allowed_categories = ['USER', 'AUCTION', 'AUCTION_ITEM']
        if categoryName not in allowed_categories:
            raise ValueError(f"Invalid category provided. Must include one of the following: {allowed_categories}")
        return categoryName
    
    def photo_subcategory(self, categoryName, subcategory):
        allowed_auction_item_subcategories = ['ITEM_PHOTO']
        if categoryName == 'AUCTION_ITEM' and subcategory not in allowed_auction_item_subcategories:
            raise ValueError(f"Invalid subcategory provided. Must include one of the following: {allowed_auction_item_subcategories}")
        
        allowed_user_subcategories = ['PROFILE_PHOTO']
        if categoryName == 'USER' and subcategory not in allowed_user_subcategories:
            raise ValueError(f"Invalid subcategory provided. Must include one of the following: {allowed_user_subcategories}")

        allowed_auction_subcategories = ['LOGO']
        if categoryName == 'AUCTION' and categoryName not in allowed_auction_subcategories:
            raise ValueError(f"Invalid subcategory provided. Must include one of the following: {allowed_auction_subcategories}")
        
        return subcategory

class User (db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    #Foreign Keys
    user_photos = db.relationship('Photo',backref='user_photos',lazy='dynamic')

    def __init__(self, first_name, last_name, email, username, password, created_at=None, updated_at=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"User has email {self.email}"

class Auction (db.Model):
    __tablename__ = "auctions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    category = db.Column(db.String(100), default='N/A', nullable=False)
    description = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    #Foreign Keys
    auction_items = db.relationship('AuctionItem',backref='auction',lazy='dynamic')
    auction_photos = db.relationship('Photo',backref='auction_photos',lazy='dynamic')


    def __init__(self, name, category, description, created_at = None, updated_at = None):
        self.name = name
        self.description = description
        self.category = self.auction_category(category)
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self):
        return f"Auction name is {self.name}"
    
    def auction_category(self, categoryName):
        allowed_categories = ['Domestic Needs', 'International Needs', 'Medical', 'Health', 'Youth']
        if categoryName not in allowed_categories:
            raise ValueError(f"Invalid category provided. Must include one of the following: {allowed_categories}")
        return categoryName
    
    def report_auction_items(self):
        print("Here are the auction items:")
        for auction_item in self.auction_items:
            print(auction_item.name)

class AuctionItem(db.Model):
    __tablename__ = 'auction_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    starting_bid = db.Column(db.Numeric(precision=10, scale=2), nullable=False, default=0)  # Assuming a precision of 10 and scale of 2 for monetary values
    bid_interval = db.Column(db.Numeric(precision=10, scale=2), nullable=False, default=0)  # Assuming a precision of 10 and scale of 2 for monetary values
    auction_start = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    auction_end = db.Column(db.DateTime, default=default_auction_end, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Foreign Keys
    auction_id = db.Column(db.Integer,db.ForeignKey('auctions.id'), nullable=False)
    auction_item_photos = db.relationship('Photo',backref='auction_item_photos',lazy='dynamic')

    # created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # auction = db.relationship('Auction', backref='auction', uselist=False) # uselist = False because 1 to 1 and not 1 to many
    # 1 to many
    # bids = db.relationship('Bid', backref='auctionItem', lazy='dynamic') #lazy describes how items should be loaded
    # 1 to 1
    # owner = db.relationship('Owner', backref='itemOwner', uselist=False) # uselist = False because 1 to 1 and not 1 to many

    def __init__(self, name, auction_id, description, starting_bid, bid_interval, auction_start=None, auction_end=None, created_at=None, updated_at=None):
        self.name = name
        self.auction_id = auction_id
        self.description = description
        self.starting_bid = starting_bid
        self.bid_interval = bid_interval
        self.auction_start = auction_start or datetime.utcnow()
        self.auction_end = auction_end or default_auction_end()
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self):
        return f"Auction item is {self.name}"
    
    def readable_auction_start(self):
        return convert_to_readable_datetime(self.auction_start)
    
    def readable_auction_end(self):
        return convert_to_readable_datetime(self.auction_end)

class Bid(db.Model):
    __tablename__ = "bids"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    ## Foreign Keys
    auction_item_id = db.Column(db.Integer,db.ForeignKey('auction_items.id'), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)

    def __init__(self, amount, auction_item_id, user_id, created_at=None, updated_at=None):
        self.amount = amount
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()
        self.auction_item_id = auction_item_id
        self.user_id = user_id
