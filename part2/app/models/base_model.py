"""Base model module."""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base class for all business logic models."""

    def __init__(self):
        """Initialize common attributes."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update object attributes from a dictionary."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

        self.save()
