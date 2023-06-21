from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import ApplicationConfig
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    # initialize all flask components and create database
    app = Flask(__name__)
    app.config.from_object(ApplicationConfig)
    from .models import User, Shelf, Category, Book

    db.init_app(app)
    bcrypt.init_app(app)
    cors = CORS(app, supports_credentials=True)
    server_session = Session(app)

    with app.app_context():
        db.create_all()

    # import and register blueprints

    # from .routes.main import main as main_blueprint

    # app.register_blueprint(main_blueprint)

    from .routes.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # from .routes.library import library as library_blueprint

    # app.register_blueprint(library_blueprint, url_prefix="/library")

    return app
