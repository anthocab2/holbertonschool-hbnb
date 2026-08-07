from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.extensions import db

from app.models.user import User



users_bp = Blueprint(
    "users",
    __name__
)



@users_bp.route(
    "/",
    methods=["POST"]
)
def create_user():

    data = request.get_json()


    if not data.get("password"):
        return jsonify(
            {
                "error": "Password required"
            }
        ), 400


    user = User(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        password=data["password"]
    )


    db.session.add(user)

    db.session.commit()


    return jsonify(
        user.to_dict()
    ), 201





@users_bp.route(
    "/",
    methods=["GET"]
)
def get_users():

    users = User.query.all()


    return jsonify(
        [
            user.to_dict()
            for user in users
        ]
    )





@users_bp.route(
    "/<user_id>",
    methods=["GET"]
)
def get_user(user_id):

    user = User.query.get(
        user_id
    )


    if not user:
        return jsonify(
            {
                "error": "Not found"
            }
        ), 404


    return jsonify(
        user.to_dict()
    )
