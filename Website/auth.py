from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import re

auth = Blueprint('auth', __name__)

# Handle POST and GET requests for login and register forms

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged In Successfully', category='success')
                login_user(user)
                return redirect(url_for('views.home'))
            else:
                flash('Password is Incorrect', category='error')
        else:
            flash('Username not Recognised', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #Regex conditions for register form fields
        usernameRegex = r'^[a-zA-Z0-9_]{5,20}$'
        emailRegex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        passwordRegex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^\da-zA-Z]).{12,}$'
        
        #Collect form data from register form fields
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #Conditional check regex

        user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()

        if user:
            flash('Username Already Exists', category='error')

        elif existing_email:
            flash('Email Already Exists', category='error')

        elif not re.match(usernameRegex, username):
            flash("Please enter a valid username (5 characters or more and alphanumeric and underscores only)", category='error')
        
        elif not re.match(emailRegex, email):
            flash("Please enter a valid email address", category='error')

        elif not re.match(passwordRegex, password1):
            flash("Please enter a valid password (12 characters minimum, lowercase, uppercase, digit, and symbol)", category='error')

        elif password1 != password2:
            flash("Password do not match", category='error')

        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')

    return render_template("register.html", user=current_user)