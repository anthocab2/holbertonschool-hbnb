# HBnB Evolution

## Description

HBnB Evolution is a simplified AirBnB-like application developed as part of the Holberton School curriculum.

The goal of this project is to design and build the foundation of a web application that allows users to manage places, amenities, and reviews through a RESTful API.

The project is developed in multiple parts. Each part focuses on a different stage of the software development process, starting with technical documentation and moving into implementation, persistence, authentication, and advanced features.

## Project Purpose

This project is designed to practice and apply important software engineering concepts, including:

* Layered architecture
* Object-oriented programming
* SOLID principles
* UML diagrams
* Facade design pattern
* RESTful API development
* Flask and flask-restx
* In-memory persistence
* API testing and validation

## Repository Structure

```text
holbertonschool-hbnb/
├── part1/
│   ├── README.md
│   ├── 0-high-level-package-diagram.md
│   ├── 1-business-logic-class-diagram.md
│   ├── 2-api-sequence-diagrams.md
│   └── 3-documentation-compilation.md
├── part2/
│   ├── app/
│   ├── tests/
│   ├── config.py
│   ├── run.py
│   ├── requirements.txt
│   ├── TESTING_REPORT.md
│   └── README.md
└── README.md
```

## Part 1: Technical Documentation

Part 1 focuses on creating technical documentation for the HBnB Evolution application.

It includes:

* A high-level package diagram
* A detailed business logic class diagram
* Sequence diagrams for main API calls
* Explanatory notes about the architecture and design decisions

The main goal of Part 1 is to create a clear blueprint before starting the implementation phase.

## Part 2: Business Logic and API Endpoints

Part 2 focuses on implementing the Presentation Layer and Business Logic Layer of the application.

It includes:

* Project setup and package initialization
* Core business logic classes
* In-memory persistence
* Facade pattern implementation
* RESTful API endpoints
* Testing and validation

The API is built using Flask and flask-restx.

## Main Entities

The application is based on four main entities:

### User

Represents a user of the application.

A user has:

* First name
* Last name
* Email
* Password
* Administrator status

### Place

Represents a property listed by a user.

A place has:

* Title
* Description
* Price
* Latitude
* Longitude
* Owner
* Amenities
* Reviews

### Amenity

Represents a feature that can be associated with a place.

Examples include:

* Wi-Fi
* Parking
* Pool
* Air conditioning

### Review

Represents feedback left by a user for a place.

A review has:

* Text
* Rating
* User
* Place

## Architecture

The project follows a layered architecture:

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

This layer exposes the RESTful API endpoints using Flask and flask-restx.

### Facade Layer

The facade provides a simplified interface between the API and the business logic.

### Business Logic Layer

This layer contains the main models and validation logic.

### Persistence Layer

In Part 2, persistence is handled with an in-memory repository.

The in-memory repository stores objects temporarily during runtime. Data is lost when the application stops.

## Technologies Used

* Python 3
* Flask
* flask-restx
* unittest
* pycodestyle
* Mermaid.js for diagrams

## Installation

From the root of the repository, go to Part 2:

```bash
cd part2
```

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

The application will run at:

```text
http://127.0.0.1:5000/
```

Swagger documentation is available at the same URL.

## Running Tests

From the `part2` directory:

```bash
python3 -m unittest discover tests
```

## Style Check

From the `part2` directory:

```bash
pycodestyle app tests config.py run.py
```

## Author

Anthony Caban