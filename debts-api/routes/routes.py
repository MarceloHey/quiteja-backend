from datetime import datetime
from typing import Optional
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

@debt.route("/", methods=["POST"])
def create_debt():
    data = request.get_json()

    existing_user_debt = Debt.query.filter_by(user_id=data["user_id"]).first()
    if existing_user_debt:
        return jsonify({"error": "Usuario ja tem divida"}), 400

    debt = Debt(
        product=data["product"],
        value=data["value"],
        user_id=data["user_id"],
        due_date=datetime.strptime(data["due_date"], "%d-%m-%Y").date(),
    )

    db.session.add(debt)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "Dívida criada com sucesso",
                "debt": {
                    "id": debt.id,
                    "product": debt.product,
                    "value": debt.value,
                    "due_date": debt.due_date,
                },
            }
        ),
        201,
    )


@debt.route("/<int:debt_id>", methods=["PATCH"])
def update_debt(debt_id):
    data = request.get_json()

    debt: Optional[Debt] = Debt.query.filter_by(id=debt_id).first()
    if not debt:
        return jsonify({"error": "Dívida não encontrada"}), 400
    
    debt.due_date = datetime.strptime(data["due_date"], "%d-%m-%Y").date()
    debt.product = data["product"]
    debt.value = data["value"]

    db.session.add(debt)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "Dívida editada com sucesso",
                "debt": {
                    "id": debt.id,
                    "product": debt.product,
                    "value": debt.value,
                    "due_date": debt.due_date,
                },
            }
        ),
        201,
    )

@debt.route("/<int:debt_id>", methods=["DELETE"])
def delete_debt(debt_id):
    debt: Optional[Debt] = Debt.query.filter_by(id=debt_id).first()
    if not debt:
        return jsonify({"error": "Dívida não encontrada"}), 400

    debtId = debt.id
    Debt.query.filter_by(id=debtId).delete()

    db.session.commit()

    return jsonify({"message": f"Dívida {debtId} removida com sucesso"}), 200
