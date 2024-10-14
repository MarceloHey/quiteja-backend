from flask import Blueprint, request, jsonify
from models.models import Debt
from app import db

# Definir um blueprint para as rotas principais
debt = Blueprint("debt", __name__, url_prefix="/debt")


@debt.route("/", methods=["GET"])
def list_debts():
    debts = Debt.query.all()  # Pega todas as dividas
    return jsonify(
        [
            {
                "id": d.id,
                "name": d.product,
                "value": d.value,
                "due_date": d.due_date.strftime("%Y-%m-%d"),
            }
            for d in debts
        ]
    )
