from abc import ABC, abstractmethod

class BaseRepository(ABC):
    """
    BaseRepository is an abstract class that defines the methods that all repositories should implement.
    """
    
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, obj_id):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass