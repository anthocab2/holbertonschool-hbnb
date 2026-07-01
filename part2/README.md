# HBnB Evolution - Part 2

## Description

This directory contains Part 2 of the HBnB Evolution project.

Part 2 focuses on implementing the Business Logic Layer and the Presentation Layer of the application using Python, Flask, and flask-restx.

The goal of this part is to bring the technical design from Part 1 to life by creating the core classes, setting up the project structure, implementing API endpoints, and testing the application.

## Objectives

The objectives of Part 2 are:

* Set up a modular Python project structure
* Implement the core business logic classes
* Implement the Facade Pattern
* Implement an in-memory persistence layer
* Build RESTful API endpoints with Flask and flask-restx
* Validate input data
* Return clear JSON responses
* Test endpoints using cURL, Swagger, and unittest

## Project Structure

```text
part2/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── amenities.py
│   │       ├── places.py
│   │       └── reviews.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py
│   │   ├── user.py
│   │   ├── amenity.py
│   │   ├── place.py
│   │   └── review.py
│   ├── persistence/
│   │   ├── __init__.py
│   │   └── repository.py
│   └── services/
│       ├── __init__.py
│       └── facade.py
├── tests/
│   ├── __init__.py
│   └── test_api.py
├── config.py
├── run.py
├── requirements.txt
├── TESTING_REPORT.md
└── README.md
```

## Architecture

Part 2 follows a layered architecture.

```text
Presentation Layer
        |
        v
Facade Layer
        |
        v
Business Logic Layer
        |
        v
Persistence Layer
```

### Presentation Layer

The Presentation Layer contains the API endpoints.

Files:

```text
app/api/v1/users.py
app/api/v1/amenities.py
app/api/v1/places.py
app/api/v1/reviews.py
```

This layer receives HTTP requests and returns JSON responses.

### Facade Layer

The facade is implemented in:

```text
app/services/facade.py
```

The facade acts as the main communication point between the API endpoints and the business logic.

### Business Logic Layer

The Business Logic Layer contains the main models.

Files:

```text
app/models/base_model.py
app/models/user.py
app/models/amenity.py
app/models/place.py
app/models/review.py
```

These classes define the attributes, validation rules, and relationships between entities.

### Persistence Layer

The Persistence Layer is implemented in:

```text
app/persistence/repository.py
```

In this part, data is stored in memory using a dictionary.

This means the data only exists while the application is running.

## Core Models

### BaseModel

`BaseModel` provides common attributes and methods for all models.

Common attributes:

* `id`
* `created_at`
* `updated_at`

Common methods:

* `save()`
* `update()`

### User

The `User` model represents an application user.

Attributes:

* `first_name`
* `last_name`
* `email`
* `password`
* `is_admin`

Validation rules:

* First name cannot be empty.
* Last name cannot be empty.
* Email must be valid.
* Email must be unique.
* Password cannot be empty.
* Password is not returned in API responses.

### Amenity

The `Amenity` model represents a feature associated with a place.

Attributes:

* `name`
* `description`

Validation rules:

* Name cannot be empty.
* Name must be 50 characters or less.
* Description must be a string.

### Place

The `Place` model represents a property listing.

Attributes:

* `title`
* `description`
* `price`
* `latitude`
* `longitude`
* `owner`
* `amenities`
* `reviews`

Validation rules:

* Title cannot be empty.
* Title must be 100 characters or less.
* Price must be zero or greater.
* Latitude must be between -90 and 90.
* Longitude must be between -180 and 180.
* Owner must be an existing user.
* Amenities must reference existing amenities.

### Review

The `Review` model represents a review left by a user for a place.

Attributes:

* `text`
* `rating`
* `user`
* `place`

Validation rules:

* Text cannot be empty.
* Rating must be an integer between 1 and 5.
* User must be an existing user.
* Place must be an existing place.

## API Endpoints

### User Endpoints

| Method | Endpoint                  | Description           |
| ------ | ------------------------- | --------------------- |
| POST   | `/api/v1/users/`          | Create a new user     |
| GET    | `/api/v1/users/`          | Retrieve all users    |
| GET    | `/api/v1/users/<user_id>` | Retrieve a user by ID |
| PUT    | `/api/v1/users/<user_id>` | Update a user         |

The DELETE operation is not implemented for users in this part.

### Amenity Endpoints

| Method | Endpoint                         | Description               |
| ------ | -------------------------------- | ------------------------- |
| POST   | `/api/v1/amenities/`             | Create a new amenity      |
| GET    | `/api/v1/amenities/`             | Retrieve all amenities    |
| GET    | `/api/v1/amenities/<amenity_id>` | Retrieve an amenity by ID |
| PUT    | `/api/v1/amenities/<amenity_id>` | Update an amenity         |

The DELETE operation is not implemented for amenities in this part.

### Place Endpoints

| Method | Endpoint                            | Description                  |
| ------ | ----------------------------------- | ---------------------------- |
| POST   | `/api/v1/places/`                   | Create a new place           |
| GET    | `/api/v1/places/`                   | Retrieve all places          |
| GET    | `/api/v1/places/<place_id>`         | Retrieve a place by ID       |
| PUT    | `/api/v1/places/<place_id>`         | Update a place               |
| GET    | `/api/v1/places/<place_id>/reviews` | Retrieve reviews for a place |

The DELETE operation is not implemented for places in this part.

### Review Endpoints

| Method | Endpoint                      | Description             |
| ------ | ----------------------------- | ----------------------- |
| POST   | `/api/v1/reviews/`            | Create a new review     |
| GET    | `/api/v1/reviews/`            | Retrieve all reviews    |
| GET    | `/api/v1/reviews/<review_id>` | Retrieve a review by ID |
| PUT    | `/api/v1/reviews/<review_id>` | Update a review         |
| DELETE | `/api/v1/reviews/<review_id>` | Delete a review         |

Reviews are the only entity with DELETE support in this part.

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

From the `part2` directory:

```bash
python3 run.py
```

The API will run at:

```text
http://127.0.0.1:5000/
```

## Swagger Documentation

Flask-restx automatically generates Swagger documentation.

After running the application, open:

```text
http://127.0.0.1:5000/
```

Expected namespaces:

* users
* amenities
* places
* reviews

## Testing with cURL

### Create a User

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
```

### List Users

```bash
curl http://127.0.0.1:5000/api/v1/users/
```

### Create an Amenity

```bash
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
-H "Content-Type: application/json" \
-d '{
  "name": "Wi-Fi",
  "description": "Wireless internet access"
}'
```

### Create a Place

Replace `USER_ID_HERE` with a valid user ID.

```bash
curl -X POST http://127.0.0.1:5000/api/v1/places/ \
-H "Content-Type: application/json" \
-d '{
  "title": "Beach House",
  "description": "Nice place near the beach",
  "price": 150.0,
  "latitude": 18.427,
  "longitude": -67.154,
  "owner_id": "USER_ID_HERE",
  "amenities": []
}'
```

### Create a Review

Replace `USER_ID_HERE` and `PLACE_ID_HERE` with valid IDs.

```bash
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
-H "Content-Type: application/json" \
-d '{
  "text": "Excellent place",
  "rating": 5,
  "user_id": "USER_ID_HERE",
  "place_id": "PLACE_ID_HERE"
}'
```

## Running Automated Tests

From the `part2` directory:

```bash
python3 -m unittest discover tests
```

Expected result:

```text
OK
```

## Style Check

Run pycodestyle:

```bash
pycodestyle app tests config.py run.py
```

## Notes

The persistence layer uses in-memory storage.

This means all created users, amenities, places, and reviews are deleted when the application stops.

In a later part of the project, this persistence layer will be replaced by a database-backed implementation.

## Author

Anthony Caban