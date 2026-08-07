import uuid

from app.extensions import db



class Review(db.Model):
    """
    Review model.
    """

    __tablename__ = "reviews"


    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )


    text = db.Column(
        db.Text,
        nullable=False
    )


    rating = db.Column(
        db.Integer,
        nullable=False
    )


    user_id = db.Column(
        db.String(36),
        db.ForeignKey("users.id"),
        nullable=False
    )


    place_id = db.Column(
        db.String(36),
        db.ForeignKey("places.id"),
        nullable=False
    )


    def to_dict(self):

        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id
        }
