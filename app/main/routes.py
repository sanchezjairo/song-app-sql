"""Import packages and modules."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from app.models import Playlist, Artist, Album, User, Song
from app.main.forms import PlaylistForm, AlbumForm, SongForm
from app import bcrypt

# Import app and db from events_app package so that we can run app
from app import app, db

main = Blueprint("main", __name__)

@main.route('/')
def homepage():
    all_songs = Song.query.all()
    all_playlist = Playlist.query.all()
    all_albums = Album.query.all()
    return render_template('home.html',
        all_songs=all_songs, all_playlist=all_playlist, all_albums=all_albums)


@main.route('/create_playlist', methods=['GET', 'POST'])
@login_required
def create_playlist():
    form = PlaylistForm()

    # if form was submitted and contained no errors
    if form.validate_on_submit(): 
        new_playlist = Playlist(
            name=form.name.data,
            publish_date=form.publish_date.data,
            songs=form.songs.data
        )
        db.session.add(new_playlist)
        db.session.commit()

        flash('New playlist was created successfully.')
        return redirect(url_for('main.playlist_detail', playlist_id=new_playlist.id))
    return render_template('create_playlist.html', form=form)

@main.route('/create_album', methods=['GET', 'POST'])
@login_required
def create_album():
    form = AlbumForm()
    if form.validate_on_submit():
        new_album = Album(
            name=form.name.data,
            publish_date=form.publish_date.data,
            songs=form.songs.data
        )
        db.session.add(new_author)
        db.session.commit()

        flash('New author created successfully.')
        return redirect(url_for('main.album_detail', album_id=new_album.id))
    
    # if form was not valid, or was not submitted yet
    return render_template('create_album.html', form=form)

@main.route('/create_song', methods=['GET', 'POST'])
@login_required
def create_song():
    form = SongForm()
    if form.validate_on_submit():
        new_song = Song(
            name=form.name.data,
            publish_date=form.publish_date.data,
            songs=form.songs.data
        )
        db.session.add(new_song)
        db.session.commit()

        flash('New song created successfully.')
        return redirect(url_for('main.song_detail', song_id=new_song.id))
    
    # if form was not valid, or was not submitted yet
    return render_template('create_song.html', form=form)