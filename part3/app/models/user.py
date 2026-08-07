from app import db
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()


class User(db.Model):
    """
    User model.
    """

    id = db.Column(
        db.String(36),
        primary_key=True
    )

    first_name = db.Column(
        db.String(50),
        nullable=False
    )

    last_name = db.Column(
        db.String(50),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(128),
        nullable=False
    )

    is_admin = db.Column(
        db.Boolean,
        default=False
    )


    def __init__(
        self,
        first_name,
        last_name,
        email,
        password,
        is_admin=False
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        # Hash password before storing
        self.password = bcrypt.generate_password_hash(
            password
        ).decode('utf-8')

        self.is_admin = is_admin


    def check_password(self, password):
        """
        Verify password.
        """

        return bcrypt.check_password_hash(
            self.password,
            password
        )


    def to_dict(self):
        """
        Convert user object to dictionary.

        Password is excluded.
        """

        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin
        }
