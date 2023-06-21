from uuid import uuid4
from . import db


def get_uuid():
    return uuid4().hex


class User(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(72), nullable=False)
    shelves = db.relationship("Shelf", backref="user")


class Shelf(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    num = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    categories = db.relationship("Category", backref="shelf")


class Category(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(4), nullable=False)
    shelf_id = db.Column(db.Integer, db.ForeignKey("shelf.id"))
    books = db.relationship("Book", backref="category")


class Book(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    binnum = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    num_in_series = db.Column(db.Integer)
    code = db.Column(db.String(15), nullable=False)
    reference = db.Column(db.String(3), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
