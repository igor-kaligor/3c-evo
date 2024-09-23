from models import db, NumberModel
from .base_repository import BaseRepository
from sqlalchemy.exc import IntegrityError

class NumberRepository(BaseRepository):
    """
    NumberRepository is a class that implements the methods defined in BaseRepository.
    """
    @staticmethod
    def add(obj):
        """
        Add a new phone number to the database
        """
        db.session.add(obj)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("A number with this value already exists.")

    @staticmethod
    def get_all():
        """
        Get all phone numbers from the database
        """
        return NumberModel.query.all()
        
    @staticmethod
    def get_all_paginated(page, per_page):
        """
        Get all phone numbers paginated from the database
        """
        return NumberModel.query.paginate(page=page, per_page=per_page)

    @staticmethod
    def get_by_id(obj_id):
        """
        Get a phone number by id from the database
        """
        return NumberModel.query.get(obj_id)

    @staticmethod
    def update(obj):
        """
        Update a phone number in the database
        """
        db.session.commit()

    @staticmethod
    def delete(obj):
        """
        Delete a phone number from the database
        """
        db.session.delete(obj)
        db.session.commit()