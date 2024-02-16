from flask import Blueprint, render_template, request, flash
import re

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usernameRegex = r'^[a-zA-Z0-9_]{5,20}$'
        emailRegex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        passwordRegex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^\da-zA-Z]).{12,}$'
        
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not re.match(usernameRegex, username):
            flash("Please enter a valid username (alphanumeric and underscores only)", category='error')
        
        elif not re.match(emailRegex, email):
            flash("Please enter a valid email address", category='error')

        elif not re.match(passwordRegex, password1):
            flash("Please enter a valid password (12 characters minimum, lowercase, uppercase, digit, and symbol)", category='error')

        elif password1 != password2:
            flash("Password do not match", category='error')

        else:
            flash('Account Created!', category='success')

    return render_template("register.html")