from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class users(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable = False)
    username = db.Column(db.String)
    email = db.Column(db.String)
    user_type = db.Column(db.String)
    password =db.Column(db.String)
    myPlaylist= db.relationship("playlist", secondary="user_playlist")

class songs(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable = False)
    name = db.Column(db.String)
    artist = db.Column(db.String)
    album = db.Column(db.String)
    year = db.Column(db.Integer)
    url = db.Column(db.String) 

class playlist(db.Model):
    __tablename__ = "playlist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable = False)
    playlistName = db.Column(db.String)
    songList = db.Column(db.String)


class user_playlist(db.Model):
    __tablename__ = "user_playlist"
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlist.id") , primary_key=True, nullable = False )
    user_id = db.Column(db.Integer,  db.ForeignKey("user.id"), primary_key=True, nullable = False)
    
    