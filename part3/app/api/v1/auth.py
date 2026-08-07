from flask import Blueprint, request, jsonify

from flask_jwt_extended import create_access_token

from app.models.user import User


auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.get_json()


    user = User.query.filter_by(
        email=data["email"]
    ).first()


    if not user:
        return jsonify(
            {
                "error": "Invalid credentials"
            }
        ), 401


    if not user.check_password(
        data["password"]
    ):
        return jsonify(
            {
                "error": "Invalid credentials"
            }
        ), 401


    token = create_access_token(
        identity=user.id
    )


    return jsonify(
        {
            "access_token": token
        }
    ), 200
