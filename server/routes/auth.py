from flask import Blueprint, request, session, jsonify
from functools import wraps
from ..models import User
from .. import db, bcrypt


auth = Blueprint("auth", __name__)


def login_required(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        user_id = session.get("user_id")

        if not user_id:
            return jsonify({"error": "Unauthorized"}), 401

        return func(*args, **kwargs)

    return check_login


@auth.route("/logout", methods=["POST"])
@login_required
def logout():
    session.pop("user_id")
    return "200"


@auth.route("/@me")
@login_required
def get_current_user():
    user = User.query.get(session.get("user_id"))

    return jsonify({"id": user.id, "username": user.username})


@auth.route("/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized"}), 401

    session["user_id"] = user.id

    return jsonify({"id": user.id, "username": user.username})


@auth.route("/signup", methods=["POST"])
def signup():
    username = request.json["username"]
    password = request.json["password"]

    user = User.query.filter_by(username=username).first()

    if user:
        return jsonify({"error": "User already exists"}), 409

    new_user = User(
        username=username,
        password=bcrypt.generate_password_hash(password),
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"id": new_user.id, "username": new_user.username})
