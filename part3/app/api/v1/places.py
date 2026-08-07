from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.extensions import db

from app.models.place import Place



places_bp = Blueprint(
    "places",
    __name__
)




@places_bp.route(
    "/",
    methods=["POST"]
)
@jwt_required()
def create_place():

    user_id = get_jwt_identity()

    data = request.get_json()


    place = Place(
        title=data["title"],
        description=data.get(
            "description"
        ),
        price=data["price"],
        latitude=data["latitude"],
        longitude=data["longitude"],
        owner_id=user_id
    )


    db.session.add(place)

    db.session.commit()


    return jsonify(
        place.to_dict()
    ), 201





@places_bp.route(
    "/",
    methods=["GET"]
)
def get_places():

    places = Place.query.all()


    return jsonify(
        [
            place.to_dict()
            for place in places
        ]
    )
