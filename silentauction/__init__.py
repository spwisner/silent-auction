import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # pip install Flask Migrate
from flask_login import LoginManager

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
app.register_blueprint(bids_blueprint, url_prefix='/bids')
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(auctions_blueprint, url_prefix='/auctions')

# login
login_manager.init_app(app)
login_manager.login_view = 'users.login'