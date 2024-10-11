from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados (SQLite)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializar o SQLAlchemy com a aplicação Flask
    db.init_app(app)

    # Registra blueprints
    from .routes import user as user_routes

    app.register_blueprint(user_routes)

    return app
