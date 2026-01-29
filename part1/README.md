# High-Level Package Diagram - HBnB

## Overview

This document describes the high-level architecture of the HBnB application.  
The application is organized using a three-layer architecture to keep the code clean, modular, and easy to maintain.

The communication between layers is handled using the Facade pattern.

---

## High-Level Package Diagram

```mermaid
classDiagram

class PresentationLayer {
    API
    Services
}

class BusinessLogicLayer {
    HBnBFacade
    User
    Place
    Review
    Amenity
}

class PersistenceLayer {
    Repositories
    Database
}

PresentationLayer --> BusinessLogicLayer : uses Facade
BusinessLogicLayer --> PersistenceLayer : data access



classDiagram

class BaseModel {
    +UUID id
    +datetime created_at
    +datetime updated_at
    +save()
    +update()
}

class User {
    +string email
    +string password
    +string first_name
    +string last_name
    +create_place()
    +add_review()
}

class Place {
    +string name
    +string description
    +float price
    +float latitude
    +float longitude
    +add_amenity()
}

class Review {
    +string text
    +int rating
}

class Amenity {
    +string name
}

BaseModel <|-- User
BaseModel <|-- Place
BaseModel <|-- Review
BaseModel <|-- Amenity

User "1" --> "many" Place : owns
User "1" --> "many" Review : writes
Place "1" --> "many" Review : receives
Place "many" --> "many" Amenity : has



