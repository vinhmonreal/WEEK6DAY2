from . import bp as app
from flask import render_template
from flask_login import login_required
from app.forms import PostForm 


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.jinja', title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja', title='About')

