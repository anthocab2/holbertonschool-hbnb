"""Place model module."""

from app.models.base_model import BaseModel
from app.models.user import User
from app.models.amenity import Amenity


class Place(BaseModel):
    """Place class representing a property listing."""

    def __init__(self, title, description, price, latitude, longitude,
                 owner):
        """Initialize a Place instance."""
        super().__init__()
        self.title = self._validate_title(title)
        self.description = self._validate_description(description)
        self.price = self._validate_price(price)
        self.latitude = self._validate_latitude(latitude)
        self.longitude = self._validate_longitude(longitude)
        self.owner = self._validate_owner(owner)
        self.reviews = []
        self.amenities = []

    def _validate_title(self, title):
        """Validate place title."""
        if not isinstance(title, str):
            raise TypeError("title must be a string")

        title = title.strip()

        if not title:
            raise ValueError("title cannot be empty")

        if len(title) > 100:
            raise ValueError("title must be 100 characters or less")

        return title

    def _validate_description(self, description):
        """Validate place description."""
        if description is None:
            return ""

        if not isinstance(description, str):
            raise TypeError("description must be a string")

        return description.strip()

    def _validate_price(self, price):
        """Validate place price."""
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")

        if price < 0:
            raise ValueError("price must be a positive number")

        return float(price)

    def _validate_latitude(self, latitude):
        """Validate place latitude."""
        if not isinstance(latitude, (int, float)):
            raise TypeError("latitude must be a number")

        if latitude < -90 or latitude > 90:
            raise ValueError("latitude must be between -90 and 90")

        return float(latitude)

    def _validate_longitude(self, longitude):
        """Validate place longitude."""
        if not isinstance(longitude, (int, float)):
            raise TypeError("longitude must be a number")

        if longitude < -180 or longitude > 180:
            raise ValueError("longitude must be between -180 and 180")

        return float(longitude)

    def _validate_owner(self, owner):
        """Validate place owner."""
        if not isinstance(owner, User):
            raise TypeError("owner must be a User instance")

        return owner

    def add_review(self, review):
        """Add a review to the place."""
        if review not in self.reviews:
            self.reviews.append(review)
            self.save()

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if not isinstance(amenity, Amenity):
            raise TypeError("amenity must be an Amenity instance")

        if amenity not in self.amenities:
            self.amenities.append(amenity)
            self.save()

    def remove_amenity(self, amenity):
        """Remove an amenity from the place."""
        if amenity in self.amenities:
            self.amenities.remove(amenity)
            self.save()

    def update(self, data):
        """Update place attributes with validation."""
        if "title" in data:
            self.title = self._validate_title(data["title"])

        if "description" in data:
            self.description = self._validate_description(
                data["description"]
            )

        if "price" in data:
            self.price = self._validate_price(data["price"])

        if "latitude" in data:
            self.latitude = self._validate_latitude(data["latitude"])

        if "longitude" in data:
            self.longitude = self._validate_longitude(data["longitude"])

        self.save()
