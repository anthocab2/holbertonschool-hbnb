"""API tests for HBnB Part 2."""

import unittest

from app import create_app
from app.services import facade


class TestHBnBAPI(unittest.TestCase):
    """Test suite for HBnB API endpoints."""

    def setUp(self):
        """Set up test client and reset in-memory storage."""
        facade.__init__()
        self.app = create_app()
        self.client = self.app.test_client()

    def create_user(self):
        """Create and return a test user."""
        response = self.client.post("/api/v1/users/", json={
            "first_name": "Anthony",
            "last_name": "Caban",
            "email": "anthony@example.com",
            "password": "1234",
            "is_admin": False
        })
        return response

    def create_amenity(self):
        """Create and return a test amenity."""
        response = self.client.post("/api/v1/amenities/", json={
            "name": "Wi-Fi",
            "description": "Wireless internet access"
        })
        return response

    def create_place(self):
        """Create and return a test place."""
        user_response = self.create_user()
        user_id = user_response.get_json()["id"]

        amenity_response = self.create_amenity()
        amenity_id = amenity_response.get_json()["id"]

        response = self.client.post("/api/v1/places/", json={
            "title": "Beach House",
            "description": "Nice place near the beach",
            "price": 150.0,
            "latitude": 18.427,
            "longitude": -67.154,
            "owner_id": user_id,
            "amenities": [amenity_id]
        })
        return response

    def create_review(self):
        """Create and return a test review."""
        place_response = self.create_place()
        place_data = place_response.get_json()
        place_id = place_data["id"]
        user_id = place_data["owner"]["id"]

        response = self.client.post("/api/v1/reviews/", json={
            "text": "Excellent place",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        return response

    def test_create_user(self):
        """Test creating a user."""
        response = self.create_user()
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["first_name"], "Anthony")
        self.assertEqual(data["last_name"], "Caban")
        self.assertEqual(data["email"], "anthony@example.com")
        self.assertNotIn("password", data)

    def test_get_all_users(self):
        """Test retrieving all users."""
        self.create_user()
        response = self.client.get("/api/v1/users/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["email"], "anthony@example.com")
        self.assertNotIn("password", data[0])

    def test_get_user_by_id(self):
        """Test retrieving a user by ID."""
        user_response = self.create_user()
        user_id = user_response.get_json()["id"]

        response = self.client.get(f"/api/v1/users/{user_id}")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], user_id)
        self.assertNotIn("password", data)

    def test_update_user(self):
        """Test updating a user."""
        user_response = self.create_user()
        user_id = user_response.get_json()["id"]

        response = self.client.put(f"/api/v1/users/{user_id}", json={
            "first_name": "Tony",
            "last_name": "Caban",
            "email": "tony@example.com",
            "password": "abcd1234",
            "is_admin": False
        })
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["first_name"], "Tony")
        self.assertEqual(data["email"], "tony@example.com")
        self.assertNotIn("password", data)

    def test_create_duplicate_user_email(self):
        """Test duplicate email validation."""
        self.create_user()
        response = self.client.post("/api/v1/users/", json={
            "first_name": "Other",
            "last_name": "User",
            "email": "anthony@example.com",
            "password": "1234",
            "is_admin": False
        })

        self.assertEqual(response.status_code, 409)

    def test_create_amenity(self):
        """Test creating an amenity."""
        response = self.create_amenity()
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["name"], "Wi-Fi")
        self.assertEqual(data["description"], "Wireless internet access")

    def test_get_all_amenities(self):
        """Test retrieving all amenities."""
        self.create_amenity()
        response = self.client.get("/api/v1/amenities/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Wi-Fi")

    def test_update_amenity(self):
        """Test updating an amenity."""
        amenity_response = self.create_amenity()
        amenity_id = amenity_response.get_json()["id"]

        response = self.client.put(f"/api/v1/amenities/{amenity_id}", json={
            "name": "Free Wi-Fi",
            "description": "Free wireless internet"
        })
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "Free Wi-Fi")

    def test_create_place(self):
        """Test creating a place."""
        response = self.create_place()
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["title"], "Beach House")
        self.assertEqual(data["price"], 150.0)
        self.assertEqual(data["owner"]["first_name"], "Anthony")
        self.assertEqual(data["amenities"][0]["name"], "Wi-Fi")

    def test_get_all_places(self):
        """Test retrieving all places."""
        self.create_place()
        response = self.client.get("/api/v1/places/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Beach House")

    def test_update_place(self):
        """Test updating a place."""
        place_response = self.create_place()
        place_id = place_response.get_json()["id"]

        response = self.client.put(f"/api/v1/places/{place_id}", json={
            "title": "Updated Beach House",
            "description": "Updated description",
            "price": 175.0,
            "latitude": 18.428,
            "longitude": -67.155,
            "amenities": []
        })
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["title"], "Updated Beach House")
        self.assertEqual(data["price"], 175.0)

    def test_create_place_invalid_price(self):
        """Test place price validation."""
        user_response = self.create_user()
        user_id = user_response.get_json()["id"]

        response = self.client.post("/api/v1/places/", json={
            "title": "Bad Place",
            "description": "Invalid price",
            "price": -10,
            "latitude": 18.427,
            "longitude": -67.154,
            "owner_id": user_id,
            "amenities": []
        })

        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_latitude(self):
        """Test place latitude validation."""
        user_response = self.create_user()
        user_id = user_response.get_json()["id"]

        response = self.client.post("/api/v1/places/", json={
            "title": "Bad Place",
            "description": "Invalid latitude",
            "price": 100,
            "latitude": 200,
            "longitude": -67.154,
            "owner_id": user_id,
            "amenities": []
        })

        self.assertEqual(response.status_code, 400)

    def test_create_review(self):
        """Test creating a review."""
        response = self.create_review()
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["text"], "Excellent place")
        self.assertEqual(data["rating"], 5)
        self.assertEqual(data["user"]["first_name"], "Anthony")
        self.assertEqual(data["place"]["title"], "Beach House")

    def test_get_all_reviews(self):
        """Test retrieving all reviews."""
        self.create_review()
        response = self.client.get("/api/v1/reviews/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["text"], "Excellent place")

    def test_update_review(self):
        """Test updating a review."""
        review_response = self.create_review()
        review_id = review_response.get_json()["id"]

        response = self.client.put(f"/api/v1/reviews/{review_id}", json={
            "text": "Updated review",
            "rating": 4
        })
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["text"], "Updated review")
        self.assertEqual(data["rating"], 4)

    def test_delete_review(self):
        """Test deleting a review."""
        review_response = self.create_review()
        review_id = review_response.get_json()["id"]

        response = self.client.delete(f"/api/v1/reviews/{review_id}")

        self.assertEqual(response.status_code, 204)

    def test_get_reviews_by_place(self):
        """Test retrieving reviews for a specific place."""
        review_response = self.create_review()
        place_id = review_response.get_json()["place"]["id"]

        response = self.client.get(f"/api/v1/places/{place_id}/reviews")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["text"], "Excellent place")

    def test_create_review_invalid_rating(self):
        """Test review rating validation."""
        place_response = self.create_place()
        place_data = place_response.get_json()
        place_id = place_data["id"]
        user_id = place_data["owner"]["id"]

        response = self.client.post("/api/v1/reviews/", json={
            "text": "Invalid rating",
            "rating": 10,
            "user_id": user_id,
            "place_id": place_id
        })

        self.assertEqual(response.status_code, 400)

    def test_create_review_empty_text(self):
        """Test review text validation."""
        place_response = self.create_place()
        place_data = place_response.get_json()
        place_id = place_data["id"]
        user_id = place_data["owner"]["id"]

        response = self.client.post("/api/v1/reviews/", json={
            "text": "",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })

        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
