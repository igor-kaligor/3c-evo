from flask import jsonify

class Response:
    
    @staticmethod
    def success(data=None, status=200):
        return jsonify(data), status

    @staticmethod
    def created(data=None):
        return jsonify(data), 201
    
    @staticmethod
    def error(message, status=400):
        return jsonify({"message": message}), status
    
    @staticmethod
    def not_found():
        return jsonify({"message": "Object not found"}), 404
    
    
    