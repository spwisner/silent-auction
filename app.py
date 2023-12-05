import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

class InfoForm(FlaskForm):
    bid = StringField('What is your bid?')
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

    form = InfoForm()

    if form.validate_on_submit():
        bid = form.bid.data

        form.bid.data = ''
    
    return render_template('bid.html', form=form, bid=bid)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')