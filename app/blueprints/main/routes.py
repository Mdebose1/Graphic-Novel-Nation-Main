from flask import render_template, current_app as app, request, redirect, url_for, flash
from datetime import datetime as dt
from app.blueprints.posts.models import Post
from app import db
from flask_login import current_user

@app.route('/', methods=['GET', 'POST'])
def home():
    print(current_user)
    if request.method =='POST':
        data = request.form.get('posts')
        p = Post(body=data, author=current_user.get_id())
        db.session.add(p)
        db.session.commit()

        flash('Nice. Your post has been created!')
        return  redirect(url_for('home'))
    return render_template('main/home.html', posts_list=[post.to_dict() for post in Post.query.order_by(Post.date_created.desc()).all()])

@app.route('/popular')
def popular():
    return 'Popular'

@app.route('/genre')
def genre():
    return 'Genre'


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method =='POST':
        data = request.form.get('posts')
        p = Post(body=data, author=current_user.get_id())
        db.session.add(p)
        db.session.commit()
        flash('Nice. Your post has been created!')
        return  redirect(url_for('profile'))
    return render_template('main/home.html', posts=[post.to_dict() for post in Post.query.filter_by(author=current_user.get_id()).order_by(Post.date_created.desc()).all()])
    
