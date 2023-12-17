import os
from flask import Flask, render_template, flash, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # pip install Flask Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db) # connects application with database

# Register blueprints
from silentauction.bids.views import bids_blueprint
from silentauction.users.views import users_blueprint
app.register_blueprint(bids_blueprint, url_prefix='/bids')
app.register_blueprint(users_blueprint, url_prefix='/users')

