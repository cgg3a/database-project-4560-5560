from flask import render_template, redirect, url_for
from app import app
from app.forms import ProfileForm

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('base.html')

@app.route('/dashboard')
def dashboard():
    return render_template('base.html')

@app.route('/games')
def games():
    return render_template('base.html')

@app.route('/search')
def search():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('login.html')