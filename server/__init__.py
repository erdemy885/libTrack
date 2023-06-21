from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import ApplicationConfig
from flask_bcrypt import Bcrypt
from flask_session import Session

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    app.config.from_object(ApplicationConfig)

    db.init_app(app)

    from .models import User, Shelf, Category, Book

    with app.app_context():
        db.create_all()

    bcrypt.init_app(app)

    server_session = Session(app)

    # from .routes.main import main as main_blueprint

    # app.register_blueprint(main_blueprint)

    from .routes.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # from .routes.library import library as library_blueprint

    # app.register_blueprint(library_blueprint, url_prefix="/library")

    return app
