from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from .. import db


auth = Blueprint('auth', __name__)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('Incorrect credentials.')
            return redirect(url_for('main.dashboard'))
        
        login_user(user, remember=remember)
        return redirect(url_for('main.home'))
    
    if request.method == 'GET':
        return render_template('credentials.html', title="Log in", current_url=request.url)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            flash('Username taken.')
            return redirect(url_for('auth.signup'))
        
        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
    if request.method == 'GET':
        return render_template('credentials.html', title="Sign up", current_url=request.url)