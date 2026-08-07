from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.extensions import db

from app.models.review import Review



reviews_bp = Blueprint(
    "reviews",
    __name__
)



@reviews_bp.route(
    "/",
    methods=["POST"]
)
@jwt_required()
def create_review():

    user_id = get_jwt_identity()

    data = request.get_json()


    review = Review(
        text=data["text"],
        rating=data["rating"],
        user_id=user_id,
        place_id=data["place_id"]
    )


    db.session.add(review)

    db.session.commit()


    return jsonify(
        review.to_dict()
    ), 201





@reviews_bp.route(
    "/",
    methods=["GET"]
)
def get_reviews():

    reviews = Review.query.all()


    return jsonify(
        [
            review.to_dict()
            for review in reviews
        
