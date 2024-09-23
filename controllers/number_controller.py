from flask import Blueprint, request
from services import NumberService
from utils.response import Response


bp = Blueprint('number', __name__, url_prefix='/api/numbers')

class NumberController:
    """
    Controller for phone numbers
    """
    @staticmethod
    @bp.route('', methods=['POST'])
    def create_object():
        """
        Create a new phone number
        """

        data = request.json
        try:
            number_obj = NumberService.create(data)

            return Response.created({"message": "Number created",
                "number": number_obj.id})
        except ValueError as e:
            return Response.error({"message": str(e)})


    @staticmethod
    @bp.route('', methods=['GET'])
    def get_objects():
        """
        Get all phone numbers
        """

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        pagination = NumberService.get_all_paginated(page, per_page)
        objects = pagination.items
        data = [{
            'id': obj.id,
            'value': obj.value,
            'monthyPrice': obj.monthyPrice,
            'setupPrice': obj.setupPrice,
            'currency': obj.currency
        } for obj in objects]
        return Response.success({
            'objects': data,
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': pagination.page,
            'per_page': pagination.per_page
        })

    @staticmethod
    @bp.route('/<int:id>', methods=['GET'])
    def get_object(id):
        """
        Get a phone number by id
        """

        obj = NumberService.get_by_id(id)
        if obj:
            data = {
                'id': obj.id,
                'value': obj.value,
                'monthyPrice': obj.monthyPrice,
                'setupPrice': obj.setupPrice,
                'currency': obj.currency
            }
            return Response.success(data)
        return Response.not_found()

    @staticmethod
    @bp.route('/<int:id>', methods=['PUT'])
    def update_object(id):
        """
        Update a phone number by id
        """
        
        data = request.json
        obj = NumberService.update(id, data)
        if obj:
            return Response.success({"message": "Number updated"})
        return Response.not_found()

    @staticmethod
    @bp.route('/<int:id>', methods=['DELETE'])
    def delete_object(id):
        """
        Delete a phone number by id
        """
        obj = NumberService.delete(id)
        if obj:
            return Response.success({"message": "Number deleted"})
        return Response.not_found()