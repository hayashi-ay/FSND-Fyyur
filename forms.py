from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import ValidationError, Optional, DataRequired, AnyOf, URL
from enums import State, Genre

def anyof_for_multiple_field(values):
  message = 'Invalid value, must be one of: {0}.'.format( ','.join(values) )

  def _validate(form, field):
    error = False
    for value in field.data:
      if value not in values:
        error = True

    if error:
      raise ValidationError(message)

  return _validate

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
        'state', validators=[DataRequired(), AnyOf( [ choice.value for choice in State ] )],
        choices=State.choices()
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link', validators=[URL(),Optional()]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired(), anyof_for_multiple_field( [ choice.value for choice in Genre ] )],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(),Optional()]
    )

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired(), AnyOf( [ choice.value for choice in State ] )],
        choices=State.choices()
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link', validators=[URL(),Optional()]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired(), anyof_for_multiple_field( [ choice.value for choice in Genre ] )],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(),Optional()]
    )