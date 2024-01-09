from silentauction import app
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, login_required,logout_user

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
