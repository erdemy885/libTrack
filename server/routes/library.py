from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required, current_user
from ..models import Shelf, Category, Book
from .. import db

library = Blueprint('library', __name__)

@library.route('/', methods=['POST', 'GET'])
@login_required
def home():
    shelves = current_user.shelves
    if request.method == 'POST':
        num = len(shelves) + 1
        new_shelf = Shelf(num=num, user=current_user)
        db.session.add(new_shelf)
        db.session.commit()
        return redirect(request.url)
    return render_template('library.html', shelves=shelves, current_url=request.url)

@library.route('/shelf/<int:shelfnum>/category/<string:catcode>', methods=['POST', 'GET'])
@login_required
def category(shelfnum, catcode):
    current_shelf = [i for i in current_user.shelves if i.num == shelfnum]
    if current_shelf:
        current_category = [i for i in current_shelf[0].categories if i.code == catcode]
        if current_category:
            books = current_category[0].books
            if request.method == 'POST':
                binnum = len([k for i in current_user.shelves for j in i.categories for k in j.books]) + 1
                title = request.form.get('title')
                author = request.form.get('author')
                num_in_series = request.form.get('num_in_series')
                reference = request.form.get('reference')
                if reference == "":
                    reference = title[:3]
                status = request.form.get('status') == 'true'
                code = str(binnum) + "-" + current_category[0].code + "+" + str(num_in_series) + reference.upper()
                new_book = Book(binnum=binnum, title=title, author=author, num_in_series=num_in_series, reference=reference.upper(), status=status, code=code, category=current_category[0])
                db.session.add(new_book)
                db.session.commit()
                return redirect(request.url)
            return render_template('category.html', data=books, current_category=current_category[0], current_url=request.url)
    return "Shelf or Category does not exist"

@library.route('/shelf/<int:shelfnum>', methods=['GET', 'POST'])
@login_required
def shelf(shelfnum):
    current_shelf = [i for i in current_user.shelves if i.num == shelfnum]
    if current_shelf:
        if request.method == 'POST': #add category
            target_shelves = request.form.getlist("target_shelves[]")
            name = request.form.get('name')
            code = request.form.get('code')
            if target_shelves:
                for shelf in target_shelves:
                    if shelf != "":
                        shelfid, catid = shelf.split(':')
                        target_shelf = Shelf.query.get(shelfid)
                        current_category = Category.query.get(catid)
                        if target_shelf.user_id == current_user.id and current_category.shelf.user_id == current_user.id:
                            current_category.shelf = target_shelf
                            db.session.add(current_category)
                        else:
                            flash('Could not move Category because either Target Shelf or Selected Category belongs to a different user')
                db.session.commit()
                return redirect(request.url)
            if name and code:
                num = len([j for i in current_user.shelves for j in i.categories]) + 1
                new_category = Category(num=num, name=name.title(), code=code.upper(), shelf=current_shelf[0])
                db.session.add(new_category)
                db.session.commit()
                return redirect(request.url)
        return render_template('shelf.html', current_shelf=current_shelf[0], categories=current_shelf[0].categories, shelves=current_user.shelves, current_url=request.url)
    return "Shelf does not exist"