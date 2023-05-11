from flask import render_template
from . import bp as app
from app.forms import RegisterForm



@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.jinja', title='Register', form = form)

@app.route('/signin')
def signin():
    return render_template('signin.jinja', title='Signin')