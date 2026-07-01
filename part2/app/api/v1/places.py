"""Place API endpoints module."""

from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace("places", description="Place operations")

owner_model = api.model("PlaceOwner", {
    "id": fields.String(readonly=True, description="Owner unique identifier"),
    "first_name": fields.String(description="Owner first name"),
    "last_name": fields.String(description="Owner last name"),
    "email": fields.String(description="Owner email")
})

amenity_model = api.model("PlaceAmenity", {
    "id": fields.String(
        readonly=True,
        description="Amenity unique identifier"
    ),
    "name": fields.String(description="Amenity name"),
    "description": fields.String(description="Amenity description")
})

place_review_user_model = api.model("PlaceReviewUser", {
    "id": fields.String(readonly=True, description="User unique identifier"),
    "first_name": fields.String(description="User first name"),
    "last_name": fields.String(description="User last name"),
    "email": fields.String(description="User email")
})

place_review_model = api.model("PlaceReview", {
    "id": fields.String(readonly=True, description="Review unique identifier"),
    "text": fields.String(description="Review text"),
    "rating": fields.Integer(description="Review rating"),
    "user": fields.Nested(
        place_review_user_model,
        description="Review author"
    ),
    "created_at": fields.DateTime(readonly=True, description="Creation date"),
    "updated_at": fields.DateTime(readonly=True, description="Update date")
})

place_model = api.model("Place", {
    "id": fields.String(readonly=True, description="Place unique identifier"),
    "title": fields.String(required=True, description="Place title"),
    "description": fields.String(description="Place description"),
    "price": fields.Float(required=True, description="Place price"),
    "latitude": fields.Float(required=True, description="Place latitude"),
    "longitude": fields.Float(required=True, description="Place longitude"),
    "owner": fields.Nested(owner_model, description="Place owner"),
    "amenities": fields.List(
        fields.Nested(amenity_model),
        description="Place amenities"
    ),
    "reviews": fields.List(
        fields.Nested(place_review_model),
        description="Place reviews"
    ),
    "created_at": fields.DateTime(readonly=True, description="Creation date"),
    "updated_at": fields.DateTime(readonly=True, description="Update date")
})

place_input_model = api.model("PlaceInput", {
    "title": fields.String(required=True, description="Place title"),
    "description": fields.String(description="Place description"),
    "price": fields.Float(required=True, description="Place price"),
    "latitude": fields.Float(required=True, description="Place latitude"),
    "longitude": fields.Float(required=True, description="Place longitude"),
    "owner_id": fields.String(required=True, description="Owner user ID"),
    "amenities": fields.List(
        fields.String,
        description="List of amenity IDs"
    )
})

place_update_model = api.model("PlaceUpdate", {
    "title": fields.String(description="Place title"),
    "description": fields.String(description="Place description"),
    "price": fields.Float(description="Place price"),
    "latitude": fields.Float(description="Place latitude"),
    "longitude": fields.Float(description="Place longitude"),
    "amenities": fields.List(
        fields.String,
        description="List of amenity IDs"
    )
})


@api.route("/")
class PlaceList(Resource):
    """Resource for creating and retrieving places."""

    @api.expect(place_input_model, validate=True)
    @api.marshal_with(place_model, code=201)
    @api.response(400, "Invalid input data")
    @api.response(404, "Owner or amenity not found")
    def post(self):
        """Create a new place."""
        place_data = api.payload

        try:
            place = facade.create_place(place_data)
        except ValueError as error:
            message = str(error)

            if "not found" in message:
                api.abort(404, message)

            api.abort(400, message)
        except TypeError as error:
            api.abort(400, str(error))

        return place, 201

    @api.marshal_list_with(place_model)
    def get(self):
        """Retrieve all places."""
        return facade.get_all_places(), 200


@api.route("/<string:place_id>")
@api.param("place_id", "Place unique identifier")
class PlaceResource(Resource):
    """Resource for retrieving and updating a specific place."""

    @api.marshal_with(place_model)
    @api.response(404, "Place not found")
    def get(self, place_id):
        """Retrieve a place by ID."""
        place = facade.get_place(place_id)

        if place is None:
            api.abort(404, "Place not found")

        return place, 200

    @api.expect(place_update_model, validate=True)
    @api.marshal_with(place_model)
    @api.response(400, "Invalid input data")
    @api.response(404, "Place or amenity not found")
    def put(self, place_id):
        """Update a place by ID."""
        place_data = api.payload

        try:
            place = facade.update_place(place_id, place_data)
        except ValueError as error:
            message = str(error)

            if "not found" in message:
                api.abort(404, message)

            api.abort(400, message)
        except TypeError as error:
            api.abort(400, str(error))

        if place is None:
            api.abort(404, "Place not found")

        return place, 200


@api.route("/<string:place_id>/reviews")
@api.param("place_id", "Place unique identifier")
class PlaceReviewList(Resource):
    """Resource for retrieving reviews associated with a place."""

    @api.marshal_list_with(place_review_model)
    @api.response(404, "Place not found")
    def get(self, place_id):
        """Retrieve all reviews for a place."""
        reviews = facade.get_reviews_by_place(place_id)

        if reviews is None:
            api.abort(404, "Place not found")

        return reviews, 200
