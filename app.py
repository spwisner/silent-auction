import os
from flask import Flask, render_template, flash, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    SubmitField, 
    BooleanField, 
    DateField, 
    RadioField, 
    SelectField, 
    TextAreaField, 
    TextField
)
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # pip install Flask Migrate

# export FLASK_APP=app.py

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
#__file__ = app.py

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
Migrate(app, db) # connects application with database



##########
# class Bid(db.Model):
#     # Manual Choice
#     __tablename__ = 'bids'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text)
#     amount = db.Column(db.Integer)
#     bid_count = db.Column(db.Integer)

#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount

#     def __repr__(self):
#         return f"Bid {self.name} has an amount of {self.amount}"

class InfoForm(FlaskForm):
    bid = StringField('What is your bid?', validators=[DataRequired()])
    is_max_bid = BooleanField("is this your max bid")
    alerts = RadioField('Do you want to be alerted for this item', choices=[('alert_zero', 'No'), ('alert_one', 'Yes')])
    interest = SelectField('What is your level of interest?', choices=[('h', 'High'), ('m', 'Medium'), ('l', 'Low')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')

@app.route('/sign-up-success')
def sign_up_success():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('sign-up-success.html', first=first, last=last)

@app.route('/bid', methods=['GET', 'POST'])
def mybid():
    bid = False
    is_max_bid = False
    alerts = False
    interest = False
    feedback = False

    form = InfoForm()

    if form.validate_on_submit():
        session['bid'] = form.bid.data
        session['is_max_bid'] = form.is_max_bid.data
        session['alerts'] = form.alerts.data
        session['interest'] = form.interest.data
        session['feedback'] = form.feedback.data

        flash('You just clicked the button')

        return redirect(url_for('bid_successful'))

    return render_template('bid.html', form=form)

@app.route('/bid-successful')
def bid_successful():
    return render_template('bid-success.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')