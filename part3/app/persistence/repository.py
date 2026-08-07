from abc import ABC, abstractmethod


class Repository(ABC):
    """
    Abstract repository.
    """


    @abstractmethod
    def add(self, obj):
        pass


    @abstractmethod
    def get(self, obj_id):
        pass


    @abstractmethod
    def get_all(self):
        pass


    @abstractmethod
    def update(self, obj_id, data):
        pass


    @abstractmethod
    def delete(self, obj_id):
        pass
