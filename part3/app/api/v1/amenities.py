from flask import Blueprint, request, jsonify

from app.extensions import db

from app.models.amenity import Amenity



amenities_bp = Blueprint(
    "amenities",
    __name__
)



@amenities_bp.route(
    "/",
    methods=["POST"]
)
def create_amenity():

    data = request.get_json()


    amenity = Amenity(
        name=data["name"]
    )


    db.session.add(amenity)

    db.session.commit()


    return jsonify(
        amenity.to_dict()
    ), 201




@amenities_bp.route(
    "/",
    methods=["GET"]
)
def get_amenities():

    amenities = Amenity.query.all()


    return jsonify(
        [
            amenity.to_dict()
            for amenity in amenities
        ]
    )
