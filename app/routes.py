from flask import render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from app import app

# Initialize the LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Example user storage (you'd likely use a database)
users = {
    "user1": {"password": "password123"},
}

# User class required by Flask-Login
class User(UserMixin):
    def __init__(self, username):
        self.id = username

# Load user function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/')
def home():
    return render_template('registration.html')

@app.route('/profile')
@login_required  # Protect this route, user must be logged in
def profile():
    return render_template('profile.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/games')
@login_required
def games():
    return render_template('games.html')

@app.route('/search')
@login_required
def search():
    return render_template('search.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        
        # Check if user exists and password is correct
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)  # Log the user in
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to the dashboard or another page
        else:
            flash('Invalid username or password', 'danger')  # Show error message on invalid login

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()  # Log the user out
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))  # Redirect to the login page

# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404