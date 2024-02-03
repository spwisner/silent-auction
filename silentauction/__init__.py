import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # pip install Flask Migrate
from flask_login import LoginManager
from flask_restful import Api

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db, render_as_batch=True) # connects application with database

# Register blueprints
from silentauction.bids.views import bids_blueprint
from silentauction.users.views import users_blueprint
from silentauction.auctions.views import auctions_blueprint
from silentauction.auction_items.views import auction_items_blueprint
from silentauction.payments.views import payments_blueprint
from silentauction.api.reset_demo import api_blueprint

app.register_blueprint(bids_blueprint, url_prefix='/bids')
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(auctions_blueprint, url_prefix='/auctions')
app.register_blueprint(auction_items_blueprint, url_prefix='/auction-items')
app.register_blueprint(payments_blueprint, url_prefix='/payments')
app.register_blueprint(api_blueprint, url_prefix='/api')

# API
api = Api(api_blueprint)

# login
login_manager.init_app(app)
login_manager.login_view = 'users.login'