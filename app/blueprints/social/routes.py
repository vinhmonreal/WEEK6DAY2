from . import bp
from app.forms import PostForm, CommentForm
from app.models import Post
from flask_login import current_user
from flask import render_template, flash, redirect, url_for

@bp.route('/post', methods=['GET','POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(body=form.body.data)
        p.id = Post.query.count() + 1
        p.user_id = current_user.user_id
        p.commit()
        flash('Published', 'success')
    return render_template('post.jinja', form = form)


@bp.route('/comments', methods=['GET','POST'])
def comments():
    form = CommentForm()
    if form.validate_on_submit():
        p = Post(body=form.body.data)
        p.id = Post.query.count() + 1
        p.user_id = 5 #my admin userid
        p.commit()
        flash('Added to my collection!', 'success')
    return render_template('comments.jinja', form = form)
        