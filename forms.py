from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL
from enums import State, Genre

class ShowForm(Form):
    # IDEA: add a number validation to artist_id and venue_id
    artist_id = StringField(
        'artist_id', validators=[DataRequired()]
    )
    venue_id = StringField(
        'venue_id', validators=[DataRequired()]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=State.choices()
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=State.choices()
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
    )

# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM
