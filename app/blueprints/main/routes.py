from . import bp as app
from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.jinja', title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja', title='About')

