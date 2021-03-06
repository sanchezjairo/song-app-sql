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
    Username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    playlist = db.relationship('Playlist', db.ForeignKey('playlist.id'), nullable=False)
    favorite_song = db.relationship('Song', secondary='user_song', back_populates='users_who_favorited')


class Song(db.Model):
    #Song model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    pubslish_date = db.Column(db.Date)
    users_who_favorited = db.relationship('User', secondary='user_song', back_populates='favorite_song')

favorite_song_table=db.Table('user_song', 
    db.Column('song_id', db.Integer, db.ForeignKey('song.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    pubslish_date = db.Column(db.Date)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    Song = db.relationship('Song', back_populates='artist')

    def __str__(self):
        return f'<Artist: {self.name}>'

    def __repr__(self):
        return f'<Artist: {self.name}>'


    





