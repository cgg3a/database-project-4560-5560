# Database Group Project for CSCI 4560/5560

In an increasingly digital world, the ability to share achievements as well as opinions has grown easier. In regards to games, there are multiple metrics for assessing a player’s success. Those metrics include but are not limited to completion time, achieved score, and developer designated  unique achievements. Our group is creating a web application that allows users to add friends and share their ratings, achievements, times, and scores in their favorite games. This application will make use of HTML, CSS, Bootstrap, and MySQL. HTML, CSS, and Bootstrap create a pleasant, simple frontend for users to enjoy while MySQL works with Flask in the backend to handle all of the data storage, organization, and requests.

### Team Members
- Caleb
- Whit
- Jordan
- Remon

## How to Run

Before starting the Flask server, we must ensure that we are working inside our virtual environment where Flask is installed.

### 1. Install pipenv if you haven't

```pipe install pipenv```

### 2. Have pipenv install a virtual environment for you

```pipenv install```

### 3. Head into the virtual environment

``` pipenv shell```

### 4. Start the Flask server

```python run.py```

### 3. Head to the URL given in your terminal

Usually, it is ```http://127.0.0.1:5000/```

### 4. Stop the server

When you're done running it, just type **exit** in your terminal.

## Project Structure

```project/
│
├── app/                     # Flask application package
│   ├── __init__.py           # Initializes the Flask app, configurations
│   ├── models.py             # Database models (SQLAlchemy)
│   ├── routes.py             # Application routes (views)
│   ├── forms.py              # Forms (Flask-WTF for handling forms)
│   ├── static/               # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   ├── fonts/
│   │   └── img/
│   └── templates/            # HTML templates (Bootstrap integrated)
│       ├── base.html         # Base layout template
│       ├── login.html      # User login page
│       ├── profile.html      # User profile page
│       └── achievements.html # Achievements display page
│
├── migrations/               # Database migration files (Flask-Migrate)
│
├── Pipfile                     # Virtual environment requirements
│
├── Pipfile.lock                     # Virtual environment hashes
│
├── config.py                 # Configuration settings
│
├── requirements.txt                # Lists all needed pips
│
└── run.py                    # Script to run the application
```
