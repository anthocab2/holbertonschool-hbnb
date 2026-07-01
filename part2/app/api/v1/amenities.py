"""Amenity API endpoints module."""

from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace("amenities", description="Amenity operations")

amenity_model = api.model("Amenity", {
    "id": fields.String(
        readonly=True,
        description="Amenity unique identifier"
    ),
    "name": fields.String(required=True, description="Amenity name"),
    "description": fields.String(description="Amenity description"),
    "created_at": fields.DateTime(readonly=True, description="Creation date"),
    "updated_at": fields.DateTime(readonly=True, description="Update date")
})

amenity_input_model = api.model("AmenityInput", {
    "name": fields.String(required=True, description="Amenity name"),
    "description": fields.String(description="Amenity description")
})

amenity_update_model = api.model("AmenityUpdate", {
    "name": fields.String(description="Amenity name"),
    "description": fields.String(description="Amenity description")
})


@api.route("/")
class AmenityList(Resource):
    """Resource for creating and retrieving amenities."""

    @api.expect(amenity_input_model, validate=True)
    @api.marshal_with(amenity_model, code=201)
    @api.response(400, "Invalid input data")
    def post(self):
        """Create a new amenity."""
        amenity_data = api.payload

        try:
            amenity = facade.create_amenity(amenity_data)
        except ValueError as error:
            api.abort(400, str(error))
        except TypeError as error:
            api.abort(400, str(error))

        return amenity, 201

    @api.marshal_list_with(amenity_model)
    def get(self):
        """Retrieve all amenities."""
        return facade.get_all_amenities(), 200


@api.route("/<string:amenity_id>")
@api.param("amenity_id", "Amenity unique identifier")
class AmenityResource(Resource):
    """Resource for retrieving and updating a specific amenity."""

    @api.marshal_with(amenity_model)
    @api.response(404, "Amenity not found")
    def get(self, amenity_id):
        """Retrieve an amenity by ID."""
        amenity = facade.get_amenity(amenity_id)

        if amenity is None:
            api.abort(404, "Amenity not found")

        return amenity, 200

    @api.expect(amenity_update_model, validate=True)
    @api.marshal_with(amenity_model)
    @api.response(400, "Invalid input data")
    @api.response(404, "Amenity not found")
    def put(self, amenity_id):
        """Update an amenity by ID."""
        amenity_data = api.payload

        try:
            amenity = facade.update_amenity(amenity_id, amenity_data)
        except ValueError as error:
            api.abort(400, str(error))
        except TypeError as error:
            api.abort(400, str(error))

        if amenity is None:
            api.abort(404, "Amenity not found")

        return amenity, 200
