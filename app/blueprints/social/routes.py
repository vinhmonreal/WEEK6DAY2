from . import bp
from app.forms import PostForm, CommentForm, AddCarForm
from app.models import Post, User, AddCar
from flask_login import current_user, login_required
from flask import render_template, flash, redirect, url_for


@bp.route('/post', methods=['GET','POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(body=form.body.data)
        p.id = Post.query.count() + 1
        p.user_id = current_user.user_id
        p.commit()
        flash('Published', 'success')
        return redirect(url_for('social.user_page', username=current_user.username))
    return render_template('post.jinja', form = form)


@bp.route('/comments', methods=['GET','POST'])
@login_required
def comments():
    form = CommentForm()
    if form.validate_on_submit():
        p = Post(body=form.body.data)
        p.id = Post.query.count() + 1
        p.user_id = 5 #my admin userid
        p.commit()
        flash('Added to my collection!', 'success')
    return render_template('comments.jinja', form = form)
        
@bp.route('/userpage/<username>')
def user_page(username):   
    user = User.query.filter_by(username=username).first()
    return render_template('user_page.jinja', title= f"{username}'s page" ,user=user)

@bp.route('/addcar', methods=['GET','POST'])
@login_required
def addcar():
    form = AddCarForm()
    if form.validate_on_submit():
        c = AddCar(make=form.make.data, model=form.model.data, year=form.year.data, info=form.info.data)
        c.user_id = current_user.user_id
        print(c.user_id)
        c.commit()
        flash('Added to car collection!', 'success')
        return redirect(url_for('social.user_page', username=current_user.username))
    return render_template('add_car.jinja', form=form)
    
