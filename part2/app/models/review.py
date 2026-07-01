"""Review model module."""

from app.models.base_model import BaseModel
from app.models.user import User


class Review(BaseModel):
    """Review class representing a user review for a place."""

    def __init__(self, text, rating, user, place):
        """Initialize a Review instance."""
        super().__init__()
        self.text = self._validate_text(text)
        self.rating = self._validate_rating(rating)
        self.user = self._validate_user(user)
        self.place = self._validate_place(place)
        self.place.add_review(self)

    def _validate_text(self, text):
        """Validate review text."""
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        text = text.strip()

        if not text:
            raise ValueError("text cannot be empty")

        return text

    def _validate_rating(self, rating):
        """Validate review rating."""
        if not isinstance(rating, int):
            raise TypeError("rating must be an integer")

        if rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")

        return rating

    def _validate_user(self, user):
        """Validate review user."""
        if not isinstance(user, User):
            raise TypeError("user must be a User instance")

        return user

    def _validate_place(self, place):
        """Validate review place."""
        from app.models.place import Place

        if not isinstance(place, Place):
            raise TypeError("place must be a Place instance")

        return place

    def update(self, data):
        """Update review attributes with validation."""
        if "text" in data:
            self.text = self._validate_text(data["text"])

        if "rating" in data:
            self.rating = self._validate_rating(data["rating"])

        self.save()
