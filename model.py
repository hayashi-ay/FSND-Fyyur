#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Show(db.Model):
  __tablename__ = 'shows'

  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), primary_key=True)
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), primary_key=True)
  start_time = db.Column(db.DateTime, nullable=False)

  venue = db.relationship('Venue')
  artist = db.relationship('Artist')

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
  web_site = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
  seeking_description = db.Column(db.String(120))

  artists = db.relationship('Artist', secondary='shows', back_populates='venues')
  shows = db.relationship('Show')

  def __repr__(self):
    return f'<Venue {self.id} {self.name}>'

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
  website = db.Column(db.String(120))
  seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
  seeking_description = db.Column(db.String(120))

  venues = db.relationship('Venue', secondary='shows', back_populates='artists')
  shows = db.relationship('Show')

  def __repr__(self):
    return f'<Artist {self.id} {self.name}>'