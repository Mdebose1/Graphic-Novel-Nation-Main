from flask import current_app as app, render_template, request, redirect, url_for, flash
from .models import User
from flask_login import login_user, logout_user
from app import db

@app.route('/posts')
def posts():
    return 'Posts'

@app.route('/user')
def user():
    return 'User'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        form_data = request.form

        email = User.query.filter_by(email=form_data.get('email')).first()
        if email is not None:
            flash('That email address is in use. Please enter a different email.')
            return redirect(url_for('register'))

        if form_data.get('password') ==form_data.get('confirm_password'):

            user = User(
                first_name=form_data.get('first_name'),
                last_name=form_data.get('last_name'),
                    email=form_data.get('email')
            )
            user.generate_password(form_data.get('password'))
            db.session.add(user)
            db.session.commit()

            login_user(user, remember=True)

            flash('Registation Successful!')
            return redirect(url_for('home'))


        else:
            flash('Passwords do not match. Please enter again.')
            return redirect(url_for('register'))
    return render_template('users/register.html')

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_data = request.form
        user = User.query.filter_by(email=form_data.get('email')).first()

        if user is None or not user.check_password(form_data.get('password')):
            flash('That email address or password cannot be found. Please try again.')
            return redirect(url_for('login'))

        login_user(user, remember=form_data.get('remember me'))
        flash('Log in successful.')
        return redirect(url_for('home'))
    return render_template('users/login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for('login'))

