from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from app.models import Artist, User, Playlist, Album, Song
from app.auth.forms import SignUpForm, LoginForm
from app import bcrypt

# Import app and db from events_app package so that we can run app
from app import app, db

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash('Account Created.')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)

@auth.route('/signup_artist', methods=['GET', 'POST'])
def signup_artist():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        artist = Artist(
            username=form.username.data,
            password=hashed_password
        )
        db.session.add(artist)
        db.session.commit()
        flash('Account Created.')
        return redirect(url_for('auth.login'))
    return render_template('signup_artist.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=True)
        next_page = request.args.get('next')
        return redirect(next_page if next_page else url_for('main.homepage'))
    return render_template('login.html', form=form)

@auth.route('/login_artist', methods=['GET', 'POST'])
def login_artist():
    form = LoginForm()
    if form.validate_on_submit():
        artist = Artist.query.filter_by(username=form.username.data).first()
        login_artist(artist, remember=True)
        next_page = request.args.get('next')
        return redirect(next_page if next_page else url_for('main.homepage'))
    return render_template('login_artist.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    logout_artist()
    flash('logged out')
    return redirect(url_for('main.homepage'))