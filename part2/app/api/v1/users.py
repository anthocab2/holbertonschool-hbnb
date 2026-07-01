"""User API endpoints module."""

from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace("users", description="User operations")

user_model = api.model("User", {
    "id": fields.String(readonly=True, description="User unique identifier"),
    "first_name": fields.String(required=True, description="User first name"),
    "last_name": fields.String(required=True, description="User last name"),
    "email": fields.String(required=True, description="User email"),
    "is_admin": fields.Boolean(description="Administrator status"),
    "created_at": fields.DateTime(readonly=True, description="Creation date"),
    "updated_at": fields.DateTime(readonly=True, description="Update date")
})

user_input_model = api.model("UserInput", {
    "first_name": fields.String(required=True, description="User first name"),
    "last_name": fields.String(required=True, description="User last name"),
    "email": fields.String(required=True, description="User email"),
    "password": fields.String(required=True, description="User password"),
    "is_admin": fields.Boolean(description="Administrator status")
})

user_update_model = api.model("UserUpdate", {
    "first_name": fields.String(description="User first name"),
    "last_name": fields.String(description="User last name"),
    "email": fields.String(description="User email"),
    "password": fields.String(description="User password"),
    "is_admin": fields.Boolean(description="Administrator status")
})


@api.route("/")
class UserList(Resource):
    """Resource for creating and retrieving users."""

    @api.expect(user_input_model, validate=True)
    @api.marshal_with(user_model, code=201)
    @api.response(400, "Invalid input data")
    @api.response(409, "Email already registered")
    def post(self):
        """Register a new user."""
        user_data = api.payload

        try:
            user = facade.create_user(user_data)
        except ValueError as error:
            message = str(error)

            if "email already registered" in message:
                api.abort(409, message)

            api.abort(400, message)
        except TypeError as error:
            api.abort(400, str(error))

        return user, 201

    @api.marshal_list_with(user_model)
    def get(self):
        """Retrieve all users."""
        return facade.get_all_users(), 200


@api.route("/<string:user_id>")
@api.param("user_id", "User unique identifier")
class UserResource(Resource):
    """Resource for retrieving and updating a specific user."""

    @api.marshal_with(user_model)
    @api.response(404, "User not found")
    def get(self, user_id):
        """Retrieve a user by ID."""
        user = facade.get_user(user_id)

        if user is None:
            api.abort(404, "User not found")

        return user, 200

    @api.expect(user_update_model, validate=True)
    @api.marshal_with(user_model)
    @api.response(400, "Invalid input data")
    @api.response(404, "User not found")
    @api.response(409, "Email already registered")
    def put(self, user_id):
        """Update a user by ID."""
        user_data = api.payload

        try:
            user = facade.update_user(user_id, user_data)
        except ValueError as error:
            message = str(error)

            if "email already registered" in message:
                api.abort(409, message)

            api.abort(400, message)
        except TypeError as error:
            api.abort(400, str(error))

        if user is None:
            api.abort(404, "User not found")

        return user, 200
