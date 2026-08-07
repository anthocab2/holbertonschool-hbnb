# HBnB Database Schema

## Entity Relationship Diagram

```mermaid
erDiagram

    USER ||--o{ PLACE : owns

    USER ||--o{ REVIEW : writes

    PLACE ||--o{ REVIEW : receives

    PLACE }o--o{ AMENITY : has



    USER {

        string id PK

        string first_name

        string last_name

        string email

        string password

        boolean is_admin

    }


    PLACE {

        string id PK

        string title

        text description

        float price

        float latitude

        float longitude

        string owner_id FK

    }


    REVIEW {

        string id PK

        text text

        integer rating

        string user_id FK

        string place_id FK

    }


    AMENITY {

        string id PK

        string name

    }

```

## Database Tables

### users

Stores application users.

Columns:

- id
- first_name
- last_name
- email
- password
- is_admin


### places

Stores properties.

Columns:

- id
- title
- description
- price
- latitude
- longitude
- owner_id


### reviews

Stores user reviews.

Columns:

- id
- text
- rating
- user_id
- place_id


### amenities

Stores available amenities.

Columns:

- id
- name


### place_amenity

Many-to-many relationship table.

Columns:

- place_id
- amenity_id