# HBnB Part 2 - Testing and Validation Report

## Introduction

This document describes the testing and validation process for the HBnB Part 2 API implementation.

The goal of this report is to verify that the implemented endpoints work correctly, return the expected status codes, follow the expected JSON response format, and properly handle invalid input.

The tests cover:

- Users
- Amenities
- Places
- Reviews

The API was tested using:

- Flask-RESTx Swagger documentation
- cURL manual requests
- Python unittest automated tests

---

## Tested Endpoints

### User Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/users/` | Create a new user |
| GET | `/api/v1/users/` | Retrieve all users |
| GET | `/api/v1/users/<user_id>` | Retrieve a user by ID |
| PUT | `/api/v1/users/<user_id>` | Update a user |

The DELETE operation is not implemented for users in this part of the project.

### Amenity Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/amenities/` | Create a new amenity |
| GET | `/api/v1/amenities/` | Retrieve all amenities |
| GET | `/api/v1/amenities/<amenity_id>` | Retrieve an amenity by ID |
| PUT | `/api/v1/amenities/<amenity_id>` | Update an amenity |

The DELETE operation is not implemented for amenities in this part of the project.

### Place Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/places/` | Create a new place |
| GET | `/api/v1/places/` | Retrieve all places |
| GET | `/api/v1/places/<place_id>` | Retrieve a place by ID |
| PUT | `/api/v1/places/<place_id>` | Update a place |
| GET | `/api/v1/places/<place_id>/reviews` | Retrieve reviews for a place |

The DELETE operation is not implemented for places in this part of the project.

### Review Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/reviews/` | Create a new review |
| GET | `/api/v1/reviews/` | Retrieve all reviews |
| GET | `/api/v1/reviews/<review_id>` | Retrieve a review by ID |
| PUT | `/api/v1/reviews/<review_id>` | Update a review |
| DELETE | `/api/v1/reviews/<review_id>` | Delete a review |

Reviews are the only entity with DELETE support in this part of the project.

---

## Validation Rules

### User Validation

- `first_name` must be a non-empty string.
- `last_name` must be a non-empty string.
- `email` must be a valid email format.
- `email` must be unique.
- `password` must be a non-empty string.
- The password is not returned in API responses.

### Amenity Validation

- `name` must be a non-empty string.
- `name` must be 50 characters or less.
- `description` must be a string.

### Place Validation

- `title` must be a non-empty string.
- `title` must be 100 characters or less.
- `price` must be a positive number or zero.
- `latitude` must be between -90 and 90.
- `longitude` must be between -180 and 180.
- `owner_id` must reference an existing user.
- Amenity IDs must reference existing amenities.

### Review Validation

- `text` must be a non-empty string.
- `rating` must be an integer between 1 and 5.
- `user_id` must reference an existing user.
- `place_id` must reference an existing place.

---

## Manual Testing with cURL

### Create User

```bash
curl -X POST http://127.0.0.1:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{
  "first_name": "Anthony",
  "last_name": "Caban",
  "email": "anthony@example.com",
  "password": "1234",
  "is_admin": false
}'