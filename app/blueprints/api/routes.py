from flask import request, jsonify, url_for, g, abort

from . import bp

from app.models import Post, User

#Recieve All Posts
@bp.get('/posts')
def api_posts():
    result = []
    for post in Post.query.all():
        result.append({
            'body': post.body,
            'author': post.author.username,
            'user_id': post.user_id,
            'post_id': post.id,
            'timestamp': post.timestamp,
        })
    return jsonify(result) 

#Recieve Post by specific username
@bp.get('/posts/<username>')
def api_posts_by_username(username):
    user = User.query.filter_by(username=username).first_or_404()
    return jsonify([{
            'body': post.body,
            'author': post.author.username,
            'user_id': post.user_id,
            'post_id': post.id,
            'timestamp': post.timestamp,
        }for post in user.posts])

#Send a single post
@bp.get('/posts/<int:id>')
def api_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({
            'body': post.body,
            'author': post.author.username,
            'user_id': post.user_id,
            'post_id': post.id,
            'timestamp': post.timestamp,
        })
    
