"""In-memory repository module."""


class InMemoryRepository:
    """Repository class for storing objects in memory."""

    def __init__(self):
        """Initialize an empty storage dictionary."""
        self._storage = {}

    def add(self, obj):
        """Add an object to the repository."""
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """Retrieve an object by its ID."""
        return self._storage.get(obj_id)

    def get_all(self):
        """Retrieve all objects from the repository."""
        return list(self._storage.values())

    def update(self, obj_id, data):
        """Update an object using a dictionary of data."""
        obj = self.get(obj_id)

        if obj is None:
            return None

        if hasattr(obj, "update"):
            obj.update(data)
        else:
            for key, value in data.items():
                setattr(obj, key, value)

        return obj

    def delete(self, obj_id):
        """Delete an object by its ID."""
        if obj_id in self._storage:
            del self._storage[obj_id]
            return True

        return False

    def get_by_attribute(self, attr_name, attr_value):
        """Retrieve an object by one of its attributes."""
        for obj in self._storage.values():
            if getattr(obj, attr_name, None) == attr_value:
                return obj

        return None
