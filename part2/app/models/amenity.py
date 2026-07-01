"""Amenity model module."""

from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class representing a place amenity."""

    def __init__(self, name, description=""):
        """Initialize an Amenity instance."""
        super().__init__()
        self.name = self._validate_name(name)
        self.description = self._validate_description(description)

    def _validate_name(self, name):
        """Validate amenity name."""
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        name = name.strip()

        if not name:
            raise ValueError("name cannot be empty")

        if len(name) > 50:
            raise ValueError("name must be 50 characters or less")

        return name

    def _validate_description(self, description):
        """Validate amenity description."""
        if description is None:
            return ""

        if not isinstance(description, str):
            raise TypeError("description must be a string")

        return description.strip()

    def update(self, data):
        """Update amenity attributes with validation."""
        if "name" in data:
            self.name = self._validate_name(data["name"])

        if "description" in data:
            self.description = self._validate_description(
                data["description"]
            )

        self.save()
