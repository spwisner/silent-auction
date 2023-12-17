from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from silentauction import db
from silentauction.models import User

users_blueprint = Blueprint('users', __name__,
                            template_folder='templates/users')

@users_blueprint.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign-up.html')

@users_blueprint.route('/sign-up-success', methods=['GET', 'POST'])
def sign_up_success():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('sign-up-success.html', first=first, last=last)
    
