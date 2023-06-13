from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Shelf, Category
from .. import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/lookup/<id>')
@login_required
def lookup(id):
    return str(id)

@main.route('/scanner')
@login_required
def scanner():
    return render_template('scanner.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)