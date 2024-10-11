from flask import Blueprint, request, jsonify

# Definir um blueprint para as rotas principais
user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/", methods=["GET"])
def list_users():
    from .models import User

    users = User.query.all()  # Pega todos os usuários
    return jsonify(
        [{"id": u.id, "name": u.name, "cpf": u.cpf, "date": u.date} for u in users]
    )


@user.route("/", methods=["POST"])
def create_user():
    from .models import User
    from . import db

    # import ipdb
    # ipdb.set_trace()

    data = request.get_json()

    existing_user = User.query.filter_by(cpf=data["cpf"]).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    user = User(
        name=data["name"],
        cpf=data["cpf"],
        date=data["date"],
    )

    db.session.add(user)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "Usuário criado com sucesso",
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "cpf": user.cpf,
                    "date": user.date,
                },
            }
        ),
        201,
    )
