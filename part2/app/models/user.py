"""User model module."""

import re
from app.models.base_model import BaseModel


class User(BaseModel):
    """User class representing an application user."""

    def __init__(self, first_name, last_name, email, password,
                 is_admin=False):
        """Initialize a User instance."""
        super().__init__()
        self.first_name = self._validate_name(first_name, "first_name")
        self.last_name = self._validate_name(last_name, "last_name")
        self.email = self._validate_email(email)
        self.password = self._validate_password(password)
        self.is_admin = bool(is_admin)

    def _validate_name(self, value, field_name):
        """Validate first name and last name."""
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")

        value = value.strip()

        if not value:
            raise ValueError(f"{field_name} cannot be empty")

        if len(value) > 50:
            raise ValueError(f"{field_name} must be 50 characters or less")

        return value

    def _validate_email(self, email):
        """Validate email format."""
        if not isinstance(email, str):
            raise TypeError("email must be a string")

        email = email.strip().lower()

        if not email:
            raise ValueError("email cannot be empty")

        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(pattern, email):
            raise ValueError("email format is invalid")

        return email

    def _validate_password(self, password):
        """Validate password."""
        if not isinstance(password, str):
            raise TypeError("password must be a string")

        if not password:
            raise ValueError("password cannot be empty")

        return password

    def update(self, data):
        """Update user attributes with validation."""
        if "first_name" in data:
            self.first_name = self._validate_name(
                data["first_name"], "first_name"
            )

        if "last_name" in data:
            self.last_name = self._validate_name(
                data["last_name"], "last_name"
            )

        if "email" in data:
            self.email = self._validate_email(data["email"])

        if "password" in data:
            self.password = self._validate_password(data["password"])

        if "is_admin" in data:
            self.is_admin = bool(data["is_admin"])

        self.save()
