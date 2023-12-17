# import os
# from flask import Flask
# from wtforms.validators import DataRequired
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate # pip install Flask Migrate
from datetime import datetime
from app import db

# export FLASK_APP=app.py

# basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)
#__file__ = app.py

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# db = SQLAlchemy(app)
# Migrate(app, db) # connects application with database

##########

class Auction (db.Model):
    __tablename__ = "auctions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Auction name is {self.name}"


class User (db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    # created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name,
        self.email = email
    
    def __repr__(self):
        return f"User has email {self.email}"

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

class AuctionItem(db.Model):
    __tablename__ = 'auction_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    # created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # auction = db.relationship('Auction', backref='auction', uselist=False) # uselist = False because 1 to 1 and not 1 to many
    # 1 to many
    # bids = db.relationship('Bid', backref='auctionItem', lazy='dynamic') #lazy describes how items should be loaded
    # 1 to 1
    # owner = db.relationship('Owner', backref='itemOwner', uselist=False) # uselist = False because 1 to 1 and not 1 to many

    def __init__(self, name):
        self.name = name
        # self.created_at = created_at
        # self.updated_at = updated_at

    def __repr__(self):
        return f"Auction item is {self.name} and owner is {self.name}"


# db.create_all()
