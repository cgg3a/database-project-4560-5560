from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#app.config.from_object('config')  # Load configuration settings from config.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Fusionman361@localhost/leaderboard' #Change password to your password for MySQL workbench
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#db = SQLAlchemy(app)  # Initialize the database
#migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Import routes after app is initialized to avoid circular imports
from app import routes, models

#Game Table
class Game(db.Model):
    __tablename__ = 'games'
    GameID = db.Column(db.Integer, primary_key=True, nullable=False)
    Title = db.Column(db.String(30))
    ReleaseDate = db.Column(db.Date)

#Version Table
class Version(db.Model):
    __tablename__ = 'versions'
    GameID = db.Column(db.Integer, db.ForeignKey('games.GameID'), primary_key=True, nullable=False)
    VersionID = db.Column(db.String(15), primary_key=True, nullable=False)
    Platform = db.Column(db.String(20))
    
    game = db.relationship('Game', backref=db.backref('versions', cascade='all, delete-orphan'))

#Category Table
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

#User Table
class User(db.Model):
    __tablename__ = 'users'
    UserID = db.Column(db.Integer, primary_key=True, nullable=False)
    Username = db.Column(db.String(20))
    Password = db.Column(db.String(20))

#Friend Table
class Friend(db.Model):
    __tablename__ = 'friends'
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True, nullable=False)
    FriendID = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True, nullable=False)

    user = db.relationship('User', foreign_keys=[UserID])
    friend = db.relationship('User', foreign_keys=[FriendID])

#Request Table
class Request(db.Model):
    __tablename__ = 'requests'
    Sender = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True, nullable=False)
    Receiver = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True, nullable=False)

    sender = db.relationship('User', foreign_keys=[Sender])
    receiver = db.relationship('User', foreign_keys=[Receiver])

#Score Table
class Score(db.Model):
    __tablename__ = 'scores'
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True, nullable=False)
    CategoryID = db.Column(db.Integer, db.ForeignKey('categories.CategoryID'), primary_key=True, nullable=False)
    Score = db.Column(db.Float)

    user = db.relationship('User', backref=db.backref('scores', cascade='all, delete-orphan'))
    category = db.relationship('Category', backref=db.backref('scores', cascade='all, delete-orphan'))

with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Error: {e}")