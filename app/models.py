# Create your models here.
from flask_login import UserMixin
from sqlalchemy_utils import URLType
from app import db
import enum
from sqlalchemy.orm import backref

class FormEnum(enum.Enum):
    """Helper class to make it easier to use enums with forms."""
    @classmethod
    def choices(cls):
        return [(choice.name, choice) for choice in cls]


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    favorite_songs = db.relationship('Song', secondary='user_song', back_populates='users_who_favorited')
    favorite_artist = db.relationship('Artist', secondary='user_artist', back_populates='users_who_favors_artist')


class Song(db.Model):
    #Song model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    publish_date = db.Column(db.Date)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artist = db.relationship('Artist', back_populates='songs')
    users_who_favorited = db.relationship('User', secondary='user_song', back_populates='favorite_songs')

favorite_song_table=db.Table('user_song', 
    db.Column('song_id', db.Integer, db.ForeignKey('song.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

favorite_artist_table=db.Table('user_artist', 
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    pubslish_date = db.Column(db.Date)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artist_album = db.relationship('Artist', back_populates='album')
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    songs = db.relationship('Song', back_populates='artist')
    album = db.relationship('Album', back_populates='artist_album')
    users_who_favors_artist = db.relationship('User', secondary='user_artist', back_populates='favorite_artist')
    


    def __str__(self):
        return f'<Artist: {self.name}>'

    def __repr__(self):
        return f'<Artist: {self.name}>'


    





