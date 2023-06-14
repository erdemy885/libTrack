from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Shelf, Category, Book
from .. import db

library = Blueprint('library', __name__)

@library.route('/', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        num = Shelf.query.filter_by(user_id=current_user.id).count() + 1
        new_shelf = Shelf(num=num, user=current_user)
        db.session.add(new_shelf)
        db.session.commit()
    shelves = current_user.shelves
    return render_template('library.html', data=shelves, current_url=request.url)

@library.route('/category/<int:catid>')
@login_required
def category(catid):
    current_category = Category.query.get(catid)
    if current_category.shelf.user_id == current_user.id:
        books = Book.query.filter_by(category_id=catid).all()
        return render_template('category.html', data=books, current_category=current_category)
    else:
        return "Restricted Access"

@library.route('/movecategory/<int:shelfid>/<int:catid>')
@login_required
def movecategory(shelfid, catid):
    target_shelf = Shelf.query.get(shelfid)
    current_category = Category.query.get(catid)
    if target_shelf.user_id == current_user.id and current_category.shelf.user_id == current_user.id:
        current_category.shelf = target_shelf
        db.session.add(current_category)
        db.session.commit()
        return redirect(url_for('library.shelf', shelfid=shelfid))
    else:
        return "Restricted Access"

@library.route('/shelf/<int:shelfid>')
@login_required
def shelf(shelfid):
    current_shelf = Shelf.query.get(shelfid)
    if current_shelf.user_id == current_user.id:
        categories = Category.query.filter_by(shelf_id=shelfid).all()
        return render_template('shelf.html', current_shelf=current_shelf, data=categories, shelves=current_user.shelves)
    else:
        return "Restricted Access"

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

        
        
