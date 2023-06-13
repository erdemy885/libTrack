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

@library.route('/shelf/<int:shelfid>')
@login_required
def shelf(shelfid):
    current_shelf = Shelf.query.get(shelfid)
    if current_shelf.user_id == current_user.id:
        categories = Category.query.filter_by(shelf_id=shelfid).all()
        return render_template('shelf.html', shelf=current_shelf, data=categories)
    else:
        return "Restricted Access"

@library.route('/addshelf')
@login_required
def addshelf():
    num = Shelf.query.filter_by(user_id=current_user.id).count() + 1
    new_shelf = Shelf(num=num, user=current_user)
    
    db.session.add(new_shelf)
    db.session.commit()

    return redirect(url_for('library.home'))

@library.route('/addcategory/<int:shelfid>', methods=['GET', 'POST'])
@login_required
def addcategory(shelfid):
    if request.method == 'GET':
        return render_template('addcategory.html')
    if request.method == 'POST':
        current_shelf = Shelf.query.get(shelfid)
        if current_shelf.user_id == current_user.id:
            name = request.form.get('name')
            code = request.form.get('code')

            num = 1
            for shelf in current_user.shelves:
                for category in shelf.categories:
                    num += 1

            new_category = Category(num=num, name=name, code=code, shelf=current_shelf)

            db.session.add(new_category)
            db.session.commit()

            return redirect(url_for('library.shelf', shelfid=shelfid))
        else:
            return "Restricted Access"

        
        
