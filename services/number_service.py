
from models import NumberModel
from repositories import NumberRepository

class NumberService:
    @staticmethod
    def create(data):
        """
        Create a new phone number
        """
        number_obj = NumberModel(
            value=data['value'],
            monthyPrice=data['monthyPrice'],
            setupPrice=data['setupPrice'],
            currency=data['currency']
        )
        NumberRepository.add(number_obj)
        return number_obj

    @staticmethod
    def get_all():
        """
        Get all phone numbers
        """
        return NumberRepository.get_all()
    @staticmethod
    def get_all_paginated(page, per_page):
        """
        Get all phone numbers paginated
        """
        return NumberRepository.get_all_paginated(page=page, per_page=per_page)


    @staticmethod
    def get_by_id(obj_id):
        """
        Get a phone number by id
        """
        return NumberRepository.get_by_id(obj_id)

    @staticmethod
    def update(obj_id, data):
        """
        Update a phone number by id
        """
        obj = NumberRepository.get_by_id(obj_id)
        if obj:
            obj.value = data['value']
            obj.monthyPrice = data['monthyPrice']
            obj.setupPrice = data['setupPrice']
            obj.currency = data['currency']
            NumberRepository.update(obj)
        return obj

    @staticmethod
    def delete(obj_id):
        """
        Delete a phone number by id
        """

        obj = NumberRepository.get_by_id(obj_id)
        if obj:
            NumberRepository.delete(obj)
        return obj