from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')  # Load configuration settings from config.py

#db = SQLAlchemy(app)  # Initialize the database
#migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Import routes after app is initialized to avoid circular imports
from app import routes, models
