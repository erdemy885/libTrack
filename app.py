from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()

if __name__ == "__main__":
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{path.join(path.dirname(path.abspath(__file__)), 'db.sqlite')}"

    db.init_app(app)

    from models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from main import main
    app.register_blueprint(main)

    from auth import auth
    app.register_blueprint(auth)

    app.run(debug=True)