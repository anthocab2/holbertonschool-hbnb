"""Facade module for the HBnB application."""

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    """Facade class used to communicate with repositories."""

    def __init__(self):
        """Initialize repositories for the main entities."""
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        """Create a new user."""
        existing_user = self.user_repo.get_by_attribute(
            "email", user_data["email"].lower()
        )

        if existing_user:
            raise ValueError("email already registered")

        user = User(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            password=user_data["password"],
            is_admin=user_data.get("is_admin", False),
        )
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Retrieve a user by ID."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Retrieve a user by email."""
        return self.user_repo.get_by_attribute("email", email.lower())

    def get_all_users(self):
        """Retrieve all users."""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """Update a user."""
        user = self.get_user(user_id)

        if user is None:
            return None

        if "email" in user_data:
            existing_user = self.get_user_by_email(user_data["email"])

            if existing_user and existing_user.id != user_id:
                raise ValueError("email already registered")

        return self.user_repo.update(user_id, user_data)

    def create_amenity(self, amenity_data):
        """Create a new amenity."""
        amenity = Amenity(
            name=amenity_data["name"],
            description=amenity_data.get("description", ""),
        )
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retrieve an amenity by ID."""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Retrieve all amenities."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Update an amenity."""
        return self.amenity_repo.update(amenity_id, amenity_data)

    def create_place(self, place_data):
        """Create a new place."""
        owner = self.get_user(place_data["owner_id"])

        if owner is None:
            raise ValueError("owner not found")

        place = Place(
            title=place_data["title"],
            description=place_data.get("description", ""),
            price=place_data["price"],
            latitude=place_data["latitude"],
            longitude=place_data["longitude"],
            owner=owner,
        )

        for amenity_id in place_data.get("amenities", []):
            amenity = self.get_amenity(amenity_id)

            if amenity is None:
                raise ValueError("amenity not found")

            place.add_amenity(amenity)

        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Retrieve a place by ID."""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Retrieve all places."""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """Update a place."""
        place = self.get_place(place_id)

        if place is None:
            return None

        amenities_ids = place_data.pop("amenities", None)
        place = self.place_repo.update(place_id, place_data)

        if amenities_ids is not None:
            amenities = []

            for amenity_id in amenities_ids:
                amenity = self.get_amenity(amenity_id)

                if amenity is None:
                    raise ValueError("amenity not found")

                amenities.append(amenity)

            place.amenities = amenities
            place.save()

        return place

    def create_review(self, review_data):
        """Create a new review."""
        user = self.get_user(review_data["user_id"])
        place = self.get_place(review_data["place_id"])

        if user is None:
            raise ValueError("user not found")

        if place is None:
            raise ValueError("place not found")

        review = Review(
            text=review_data["text"],
            rating=review_data["rating"],
            user=user,
            place=place,
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        """Retrieve a review by ID."""
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        """Retrieve all reviews."""
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        """Retrieve reviews for a specific place."""
        place = self.get_place(place_id)

        if place is None:
            return None

        return place.reviews

    def update_review(self, review_id, review_data):
        """Update a review."""
        return self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        """Delete a review."""
        review = self.get_review(review_id)

        if review is None:
            return False

        if review in review.place.reviews:
            review.place.reviews.remove(review)
            review.place.save()

        return self.review_repo.delete(review_id)
