# HBnB Part 3

## Description

HBnB is a backend REST API inspired by Airbnb.

Part 3 introduces:

- User authentication
- JWT authorization
- Password hashing
- SQLAlchemy ORM
- SQLite database
- Database relationships
- Repository pattern


## Technologies

- Python 3
- Flask
- Flask-JWT-Extended
- Flask-Bcrypt
- Flask-SQLAlchemy
- SQLite
- MySQL compatible


## Project Structure

```
part3/

├── app/

│   ├── api/

│   │   └── v1/

│   │       ├── auth.py

│   │       ├── users.py

│   │       ├── places.py

│   │       ├── reviews.py

│   │       └── amenities.py


│   ├── models/

│   ├── persistence/

│   ├── services/

│   └── extensions.py


├── config.py

├── run.py

├── schema.md

└── requirements.txt
```


## Installation


Clone repository:

```bash
git clone https://github.com/holbertonschool/holbertonschool-hbnb.git
```


Enter project:

```bash
cd holbertonschool-hbnb/part3
```


Install dependencies:

```bash
pip3 install -r requirements.txt
```


## Running the Application


Start server:

```bash
python3 run.py
```


Application runs:

```
http://127.0.0.1:5000
```


## Authentication

HBnB uses JWT authentication.

Users login using:

```
POST /api/v1/auth/login
```


Example:

```json
{
    "email": "user@test.com",
    "password": "password"
}
```


Response:

```json
{
    "access_token": "JWT_TOKEN"
}
```


Protected endpoints require:

```
Authorization: Bearer TOKEN
```


## API Endpoints


### Users

Create user:

```
POST /api/v1/users/
```


Get users:

```
GET /api/v1/users/
```



### Places

Create place:

```
POST /api/v1/places/
```

Requires JWT.


Get places:

```
GET /api/v1/places/
```



### Reviews

Create review:

```
POST /api/v1/reviews/
```

Requires JWT.



### Amenities

Create amenity:

```
POST /api/v1/amenities/
```


Get amenities:

```
GET /api/v1/amenities/
```



## Database

Development:

```
SQLite
```


Production:

```
MySQL
```


SQLAlchemy handles ORM mapping between Python objects and database tables.


## Security Features

Implemented:

- Password hashing with bcrypt
- JWT authentication
- Protected routes
- Role based administration support


## Database Diagram

See:

```
schema.md
```


## Author

Anthony Caban

Holberton School