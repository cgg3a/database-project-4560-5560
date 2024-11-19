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