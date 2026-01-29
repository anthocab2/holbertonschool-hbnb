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
