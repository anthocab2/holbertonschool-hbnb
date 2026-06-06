# 3. Documentation Compilation

## Objective

The objective of this document is to compile all diagrams and explanatory notes into a comprehensive technical document.

This document brings together the architecture, business logic design, and API interaction flow for the HBnB Evolution application.

It serves as a reference for the next implementation phases of the project.

---

## Introduction

HBnB Evolution is a simplified AirBnB-like application.

The application allows users to:

- Register and manage profile information
- Create and manage places
- Submit reviews for places
- Manage amenities associated with places

This documentation explains the architecture and design decisions used to structure the system.

---

## Included Documents

The technical documentation is divided into the following files:

- `0-high-level-package-diagram.md`
- `1-business-logic-class-diagram.md`
- `2-api-sequence-diagrams.md`

These files contain the main diagrams and explanatory notes required for Part 1 of the project.

---

## High-Level Architecture Summary

The HBnB Evolution application follows a layered architecture.

The main layers are:

1. Presentation Layer
2. Business Logic Layer
3. Persistence Layer

### Presentation Layer

The Presentation Layer receives user requests through APIs and services.

It handles requests such as:

- User registration
- Place creation
- Review submission
- Fetching places
- Managing amenities

### Business Logic Layer

The Business Logic Layer contains the main models and business rules.

The key entities are:

- `User`
- `Place`
- `Review`
- `Amenity`

This layer validates and manages the behavior of these entities.

### Persistence Layer

The Persistence Layer stores and retrieves data.

It is responsible for database-related operations such as saving, updating, deleting, and retrieving objects.

---

## Facade Pattern Summary

The `HBnBFacade` is used as an interface between the Presentation Layer and the Business Logic Layer.

The facade provides a simplified way for the API to interact with the business logic.

Instead of the API directly calling multiple models, the API calls methods from the facade.

Examples of facade methods include:

- `register_user()`
- `create_place()`
- `submit_review()`
- `list_places()`
- `manage_amenities()`

This design reduces coupling and improves maintainability.

---

## Business Logic Summary

The Business Logic Layer contains the main entities of the application.

A `BaseModel` class is included to provide shared attributes and methods to all entities.

Common attributes include:

- `id`
- `created_at`
- `updated_at`

Common methods include:

- `save()`
- `update()`
- `delete()`

The main entities inherit from `BaseModel`.

---

## Entity Relationship Summary

The relationships between entities are based on the business rules of the application.

### User and Place

A user can own many places.

Each place belongs to one user.

### User and Review

A user can write many reviews.

Each review belongs to one user.

### Place and Review

A place can receive many reviews.

Each review belongs to one place.

### Place and Amenity

A place can have many amenities.

An amenity can be associated with many places.

This is a many-to-many relationship.

---

## API Interaction Flow Summary

The sequence diagrams describe how API requests move through the application layers.

The documented API calls are:

1. User Registration
2. Place Creation
3. Review Submission
4. Fetching a List of Places

Each request follows a similar flow:

1. The user sends a request to the API.
2. The API forwards the request to the `HBnBFacade`.
3. The facade coordinates the operation with the Business Logic Layer.
4. The Business Logic Layer validates and processes the request.
5. The Persistence Layer stores or retrieves data when needed.
6. The response is returned through the facade.
7. The API returns the final response to the user.

---

## Design Decisions

### Layered Architecture

The layered architecture was chosen to separate responsibilities.

This makes the application easier to understand, test, and maintain.

Each layer has a specific role, which avoids mixing API logic, business rules, and database operations.

### Facade Pattern

The facade pattern was chosen to simplify communication between layers.

It provides a single entry point to the Business Logic Layer.

This makes the system more organized and easier to extend.

### BaseModel

The `BaseModel` class was added to centralize common attributes and methods.

This avoids repetition and ensures that all main entities have a consistent structure.

### UML Diagrams

UML diagrams were used to provide a clear visual representation of the system.

The diagrams help explain:

- System architecture
- Entity structure
- Entity relationships
- API request flow

---

## Conclusion

This documentation provides a complete technical overview of Part 1 of the HBnB Evolution project.

It includes:

- A high-level package diagram
- A detailed class diagram for the Business Logic Layer
- Four sequence diagrams for important API calls
- Explanatory notes for the architecture and design decisions

This document will guide the implementation of the HBnB Evolution application in the next phases of the project.