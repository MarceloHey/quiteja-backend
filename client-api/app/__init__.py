from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

# Configuração do banco de dados (SQLite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar o SQLAlchemy com a aplicação Flask
db = SQLAlchemy(app=app)

from routes.routes import user as user_routes

app.register_blueprint(user_routes)
