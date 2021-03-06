"""Import packages and modules."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from app.models import Playlist, Artist, Album, User, Song
from app.main.forms import PlaylistForm, AlbumForm, SongForm, ArtistForm
from app import bcrypt

# Import app and db from events_app package so that we can run app
from app import app, db

main = Blueprint("main", __name__)

@main.route('/')
def homepage():
    all_songs = Song.query.all()
    all_playlist = Playlist.query.all()
    all_albums = Album.query.all()
    all_artist = Artist.query.all()
    return render_template('base.html',
        all_songs=all_songs, all_playlist=all_playlist, all_albums=all_albums, all_artist=all_artist)


@main.route('/create_playlist', methods=['GET', 'POST'])
@login_required
def create_playlist():
    form = PlaylistForm()

    # if form was submitted and contained no errors
    if form.validate_on_submit(): 
        new_playlist = Playlist(
            name=form.name.data,
            songs_in_playlist=form.songs_in_playlist.data
        )
        db.session.add(new_playlist)
        db.session.commit()

        flash('New playlist was created successfully.')
        return redirect(url_for('main.homepage', playlist_id=new_playlist.id))
    return render_template('create_playlist.html', form=form)

@main.route('/create_artist', methods=['GET', 'POST'])
@login_required
def create_artist():
    form = ArtistForm()

    # if form was submitted and contained no errors
    if form.validate_on_submit(): 
        new_artist = Artist(
            name=form.name.data
        )
        db.session.add(new_artist)
        db.session.commit()

        flash('New artist was created successfully.')
        return redirect(url_for('main.homepage'))
    return render_template('create_artist.html', form=form)



@main.route('/create_album', methods=['GET', 'POST'])
@login_required
def create_album():
    form = AlbumForm()
    if form.validate_on_submit():
        new_album = Album(
            name_album=form.name.data,
            publish_date=form.publish_date.data,
            songs=form.songs.data
        )
        db.session.add(new_album)
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
            title=form.title.data,
            publish_date=form.publish_date.data,
            artist=form.artist.data
        )
        db.session.add(new_song)
        db.session.commit()

        flash('New song created successfully.')
        return redirect(url_for('main.homepage', song_id=new_song.id))
    
    # if form was not valid, or was not submitted yet
    return render_template('create_song.html', form=form)

@main.route('/song/<song_id>', methods=['GET', 'POST'])
def song_detail(song_id):
    song = Song.query.get(song_id)
    form = SongForm(obj=song)
    
    # if form was submitted and contained no errors
    if form.validate_on_submit():
        song.title = form.title.data
        song.publish_date = form.publish_date.data
        song.artist = form.artist.data

        db.session.commit()

        flash('Song was updated successfully.')
        return redirect(url_for('main.Song_detail', song_id=song_id))

    return render_template('song_detail.html', song=song, form=form)

@main.route('/artist/<artist_id>', methods=['GET', 'POST'])
def artist_detail(artist_id):
    artist = Artist.query.get(artist_id)
    form = ArtistForm(obj=artist)
    
    # if form was submitted and contained no errors
    if form.validate_on_submit():
        artist.name = form.name.data

        db.session.commit()

        flash('Artist was updated successfully.')
        return redirect(url_for('main.artist_detail', artist_id=artist_id))

    return render_template('artist_detail.html', artist=artist, form=form)

@main.route('/favorite/<song_id>', methods=['POST'])
@login_required
def favorite_song(song_id):
    song = Song.query.get(song_id)
    if song in current_user.favorite_songs:
        flash('Song already in favorites.')
    else:
        current_user.favorite_songs.append(song)
        db.session.add(current_user)
        db.session.commit()
        flash('Song added to favorites.')
    return redirect(url_for('main.song_detail', song_id=song_id))


@main.route('/unfavorite/<song_id>', methods=['POST'])
@login_required
def unfavorite_song(song_id):
    song = Song.query.get(song_id)
    if song not in current_user.favorite_songs:
        flash('Book not in favorites.')
    else:
        current_user.favorite_songs.remove(song)
        db.session.add(current_user)
        db.session.commit()
        flash('Song removed from favorites.')
    return redirect(url_for('main.song_detail', song_id=song_id))

@main.route('/favorite/<artist_id>', methods=['POST'])
@login_required
def favorite_artist(artist_id):
    artist = Artist.query.get(artist_id)
    if artist in current_user.favorite_artist:
        flash('Song already in favorites.')
    else:
        current_user.favorite_artist.append(artist)
        db.session.add(current_user)
        db.session.commit()
        flash('Artist added to favorites.')
    return redirect(url_for('main.song_detail', artist_id=artist_id))


@main.route('/unfavorite/<song_id>', methods=['POST'])
@login_required
def unfavorite_artist(song_id):
    song = Song.query.get(song_id)
    if song not in current_user.favorite_songs:
        flash('Book not in favorites.')
    else:
        current_user.favorite_songs.remove(song)
        db.session.add(current_user)
        db.session.commit()
        flash('Song removed from favorites.')
    return redirect(url_for('main.song_detail', song_id=song_id))