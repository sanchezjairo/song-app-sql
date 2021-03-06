from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import User, Albums, Song, Playlist

class SongForm(FlaskForm):

    """Form to create song"""
    name = StringField('Song Name', validators=[DataRequired(), Length(min=3 max=80)])
    publish_date = DateField('Date Published')
    artist = QuerySelectField('Artist',
        query_factory=lambda: Artist.query, allow_blank=False)
    submit = SubmitField('Submit')


class Album(FlaskForm):
    """Form to create album"""
    name = StringField('Album Name', validators=[DataRequired(), Length(min=3 max=80)])
    publish_date = DateField('Date Published')
    songs = StringField('Song Name', validators=[DataRequired(), Length(min=3 max=80)])
    artist = QuerySelectField('Artist',
        query_factory=lambda: Artist.query, allow_blank=False)
    submit = SubmitField('Submit')

class Playlist(FlaskForm):
    """Form to create Playlist"""
    name = StringField('Album Name', validators=[DataRequired(), Length(min=3 max=80)])
    publish_date = DateField('Date Published')
    songs = StringField('Song Name', validators=[DataRequired(), Length(min=3 max=80)])
    user = QuerySelectField('User',
        query_factory=lambda: Artist.query, allow_blank=False)


