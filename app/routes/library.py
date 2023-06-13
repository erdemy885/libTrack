from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Shelf, Category
from .. import db

library = Blueprint('library', __name__)

@library.route('/')
@login_required
def home():
    shelves = Shelf.query.filter_by(user_id=current_user.id).all()
    return render_template('library.html', data=shelves)

@library.route('/addshelf')
@login_required
def addshelf():
    num = Shelf.query.filter_by(user_id=current_user.id).count() + 1
    new_shelf = Shelf(num=num, user=current_user)
    
    db.session.add(new_shelf)
    db.session.commit()

    return redirect(url_for('library.home'))