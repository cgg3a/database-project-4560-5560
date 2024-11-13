# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

# Initialize the Flask app
app = Flask(__name__)

# Load configuration from the config object
app.config.from_object(config)

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes and models after initializing app to avoid circular imports
from app import routes, models

# Define your models here or import them from another file
class Game(db.Model):
    __tablename__ = 'games'
    GameID = db.Column(db.Integer, primary_key=True, nullable=False)
    Title = db.Column(db.String(30))
    ReleaseDate = db.Column(db.Date)

class Version(db.Model):
    __tablename__ = 'versions'
    GameID = db.Column(db.Integer, db.ForeignKey('games.GameID'), primary_key=True, nullable=False)
    VersionID = db.Column(db.String(15), primary_key=True, nullable=False)
    Platform = db.Column(db.String(20))
    
    game = db.relationship('Game', backref=db.backref('versions', cascade='all, delete-orphan'))

class Category(db.Model):
    __tablename__ = 'categories'
    CategoryID = db.Column(db.Integer, primary_key=True, nullable=False)
    GameID = db.Column(db.Integer, nullable=False)
    VersionID = db.Column(db.String(15), nullable=False)
    Name = db.Column(db.String(30))
    Description = db.Column(db.String(100))
    Type = db.Column(db.String(15))

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['GameID', 'VersionID'],
            ['versions.GameID', 'versions.VersionID']
        ),
    )

    version = db.relationship('Version', backref=db.backref('categories', cascade='all, delete-orphan'))

class User(db.Model):
    __tablename__ = 'users'
    UserID = db.Column(db.Integer, primary_key=True, nullable=False)
    Username = db.Column(db.String(20))
    Password = db.Column(db.String(20))

class Friend(db.Model):
    __tablename__ = 'friends'
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True, nullable=False)
    FriendID = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True, nullable=False)

    user = db.relationship('User', foreign_keys=[UserID])
    friend = db.relationship('User', foreign_keys=[FriendID])

class Request(db.Model):
    __tablename__ = 'requests'
    Sender = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True, nullable=False)
    Receiver = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True, nullable=False)

    sender = db.relationship('User', foreign_keys=[Sender])
    receiver = db.relationship('User', foreign_keys=[Receiver])

class Score(db.Model):
    __tablename__ = 'scores'
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True, nullable=False)
    CategoryID = db.Column(db.Integer, db.ForeignKey('categories.CategoryID'), primary_key=True, nullable=False)
    Score = db.Column(db.Float)

    user = db.relationship('User', backref=db.backref('scores', cascade='all, delete-orphan'))
    category = db.relationship('Category', backref=db.backref('scores', cascade='all, delete-orphan'))