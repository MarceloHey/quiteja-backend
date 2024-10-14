from flask import Flask
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

# Configuração do banco de dados (SQLite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///debts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app=app)

from routes.routes import debt as debt_routes

app.register_blueprint(debt_routes)
