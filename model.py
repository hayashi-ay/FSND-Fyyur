#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
shows = db.Table('shows',
  db.Column('start_time', db.DateTime, nullable=False),
  db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'), primary_key=True),
  db.Column('venue_id', db.Integer, db.ForeignKey('venues.id'), primary_key=True)
)

class Venue(db.Model):
  __tablename__ = 'venues'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  address = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  artists = db.relationship('Artist', secondary=shows, backref=db.backref('artists', lazy=True))

class Artist(db.Model):
  __tablename__ = 'artists'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  genres = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))