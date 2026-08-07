import uuid

from app.extensions import db



class Amenity(db.Model):
    """
    Amenity model.
    """

    __tablename__ = "amenities"


    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )


    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )


    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name
        }
