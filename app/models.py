from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    shelves = db.relationship('Shelf', backref='user')

class Shelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    categories = db.relationship('Category', backref='shelf')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(5), nullable=False)
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelf.id'))
    books = db.relationship('Book', backref='category')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    num_in_series = db.Column(db.Integer)
    code = db.Column(db.String(15), nullable=False)
    reference = db.Column(db.String(15), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))