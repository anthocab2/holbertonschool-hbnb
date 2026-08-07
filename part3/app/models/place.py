import uuid

from app.extensions import db


place_amenity = db.Table(
    "place_amenity",

    db.Column(
        "place_id",
        db.String(36),
        db.ForeignKey("places.id")
    ),

    db.Column(
        "amenity_id",
        db.String(36),
        db.ForeignKey("amenities.id")
    )
)



class Place(db.Model):
    """
    Place model.
    """

    __tablename__ = "places"


    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )


    title = db.Column(
        db.String(100),
        nullable=False
    )


    description = db.Column(
        db.Text,
        nullable=True
    )


    price = db.Column(
        db.Float,
        nullable=False
    )


    latitude = db.Column(
        db.Float,
        nullable=False
    )


    longitude = db.Column(
        db.Float,
        nullable=False
    )


    owner_id = db.Column(
        db.String(36),
        db.ForeignKey("users.id"),
        nullable=False
    )


    reviews = db.relationship(
        "Review",
        backref="place",
        lazy=True,
        cascade="all, delete"
    )


    amenities = db.relationship(
        "Amenity",
        secondary=place_amenity,
        lazy="subquery",
        backref=db.backref(
            "places",
            lazy=True
        )
    )


    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id
        }
