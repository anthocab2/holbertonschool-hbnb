"""Review API endpoints module."""

from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace("reviews", description="Review operations")

review_user_model = api.model("ReviewUser", {
    "id": fields.String(readonly=True, description="User unique identifier"),
    "first_name": fields.String(description="User first name"),
    "last_name": fields.String(description="User last name"),
    "email": fields.String(description="User email")
})

review_place_model = api.model("ReviewPlace", {
    "id": fields.String(readonly=True, description="Place unique identifier"),
    "title": fields.String(description="Place title")
})

review_model = api.model("Review", {
    "id": fields.String(readonly=True, description="Review unique identifier"),
    "text": fields.String(required=True, description="Review text"),
    "rating": fields.Integer(required=True, description="Review rating"),
    "user": fields.Nested(review_user_model, description="Review user"),
    "place": fields.Nested(review_place_model, description="Reviewed place"),
    "created_at": fields.DateTime(readonly=True, description="Creation date"),
    "updated_at": fields.DateTime(readonly=True, description="Update date")
})

review_input_model = api.model("ReviewInput", {
    "text": fields.String(required=True, description="Review text"),
    "rating": fields.Integer(required=True, description="Review rating"),
    "user_id": fields.String(required=True, description="User ID"),
    "place_id": fields.String(required=True, description="Place ID")
})

review_update_model = api.model("ReviewUpdate", {
    "text": fields.String(description="Review text"),
    "rating": fields.Integer(description="Review rating")
})


@api.route("/")
class ReviewList(Resource):
    """Resource for creating and retrieving reviews."""

    @api.expect(review_input_model, validate=True)
    @api.marshal_with(review_model, code=201)
    @api.response(400, "Invalid input data")
    @api.response(404, "User or place not found")
    def post(self):
        """Create a new review."""
        review_data = api.payload

        try:
            review = facade.create_review(review_data)
        except ValueError as error:
            message = str(error)

            if "not found" in message:
                api.abort(404, message)

            api.abort(400, message)
        except TypeError as error:
            api.abort(400, str(error))

        return review, 201

    @api.marshal_list_with(review_model)
    def get(self):
        """Retrieve all reviews."""
        return facade.get_all_reviews(), 200


@api.route("/<string:review_id>")
@api.param("review_id", "Review unique identifier")
class ReviewResource(Resource):
    """Resource for retrieving, updating, and deleting a review."""

    @api.marshal_with(review_model)
    @api.response(404, "Review not found")
    def get(self, review_id):
        """Retrieve a review by ID."""
        review = facade.get_review(review_id)

        if review is None:
            api.abort(404, "Review not found")

        return review, 200

    @api.expect(review_update_model, validate=True)
    @api.marshal_with(review_model)
    @api.response(400, "Invalid input data")
    @api.response(404, "Review not found")
    def put(self, review_id):
        """Update a review by ID."""
        review_data = api.payload

        try:
            review = facade.update_review(review_id, review_data)
        except ValueError as error:
            api.abort(400, str(error))
        except TypeError as error:
            api.abort(400, str(error))

        if review is None:
            api.abort(404, "Review not found")

        return review, 200

    @api.response(204, "Review deleted")
    @api.response(404, "Review not found")
    def delete(self, review_id):
        """Delete a review by ID."""
        deleted = facade.delete_review(review_id)

        if not deleted:
            api.abort(404, "Review not found")

        return "", 204
