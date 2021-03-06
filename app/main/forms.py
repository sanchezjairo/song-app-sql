from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import User, Album, Song, Playlist, Artist

class SongForm(FlaskForm):

    """Form to create song"""
    title = StringField('Song Name', validators=[DataRequired(), Length(min=3, max=80)])
    publish_date = DateField('Date Published')
    artist = QuerySelectField('Artist',
        query_factory=lambda: Artist.query, allow_blank=False)
    submit = SubmitField('Submit')


class AlbumForm(FlaskForm):
    """Form to create album"""
    name_album = StringField('Album Name', validators=[DataRequired(), Length(min=3, max=80)])
    publish_date = DateField('Date Published')
    songs = StringField('Song Name', validators=[DataRequired(), Length(min=3, max=80)])
    artist = QuerySelectField('Artist',
        query_factory=lambda: Artist.query, allow_blank=False)
    submit = SubmitField('Submit')

class PlaylistForm(FlaskForm):
    """Form to create Playlist"""
    name = StringField('Album Name', validators=[DataRequired(), Length(min=3, max=80)])
    songs_in_playlist = StringField('Song name', validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit')

class ArtistForm(FlaskForm):
    name = StringField('Album Name', validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit')


