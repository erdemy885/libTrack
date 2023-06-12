from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Category
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

@main.route('/newcategory', methods=['GET', 'POST'])
@login_required
def create_category():
    if request.method == 'POST':
        num = Category.query.filter_by(user_id=current_user.id).count() + 1
        name = request.form.get('name')
        code = request.form.get('code')
        shelf = request.form.get('shelf')

        new_category = Category(num=num, name=name, code=code, shelf=shelf, user=current_user)

        db.session.add(new_category)
        db.session.commit()

        return redirect(url_for('main.dashboard'))
    if request.method == 'GET':
        return render_template('create_category.html')