# HBnB Part 1 - Compact Technical Documentation

```mermaid
%% High-Level Package Diagram
classDiagram
class PresentationLayer { API Services }
class BusinessLogicLayer { HBnBFacade User Place Review Amenity }
class PersistenceLayer { Repositories Database }
PresentationLayer --> BusinessLogicLayer : uses Facade
BusinessLogicLayer --> PersistenceLayer : data access

%% Detailed Class Diagram
class BaseModel { +UUID id +datetime created_at +datetime updated_at +save() +update() }
class User { +string email +string password +string first_name +string last_name +create_place() +add_review() }
class Place { +string name +string description +float price +float latitude +float longitude +add_amenity() }
class Review { +string text +int rating }
class Amenity { +string name }
BaseModel <|-- User
BaseModel <|-- Place
BaseModel <|-- Review
BaseModel <|-- Amenity
User "1" --> "many" Place : owns
User "1" --> "many" Review : writes
Place "1" --> "many" Review : receives
Place "many" --> "many" Amenity : has

%% Sequence Diagram - User Registration
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database
User->>API: POST /register (email, password)
API->>BusinessLogic: validate input
BusinessLogic->>Database: save new User
Database-->>BusinessLogic: confirm save
BusinessLogic-->>API: return success
API-->>User: account created

%% Sequence Diagram - Place Creation
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database
User->>API: POST /places (name, description, price, etc.)
API->>BusinessLogic: validate place data
BusinessLogic->>Database: save new Place
Database-->>BusinessLogic: confirm save
BusinessLogic-->>API: return success
API-->>User: place created

%% Sequence Diagram - Review Submission
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database
User->>API: POST /reviews (place_id, text, rating)
API->>BusinessLogic: validate review
BusinessLogic->>Database: save Review
Database-->>BusinessLogic: confirm save
BusinessLogic-->>API: return success
API-->>User: review submitted

%% Sequence Diagram - Fetching List of Places
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database
User->>API: GET /places?filter=...
API->>BusinessLogic: apply filters and retrieve data
BusinessLogic->>Database: query places
Database-->>BusinessLogic: return results
BusinessLogic-->>API: formatted place list
API-->>User: return place list
