from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.create_office import ModelOffice, offices
offices = Blueprint('offices', __name__)


class Office:
    """
     Create government office.
    """
    @office.route('/offices', methods=['POST'])
    def post():
        create = ModelOffice().save(name,type)
        return jsonify({
            "message": "office created successfully!",
            "id": len(offices)
            }), 201

    """
     Fetch all the existing offices.
    """
    @office.route('/offices', methods=['GET']) 
    def get_offices():
        return make_response(jsonify({
            "message": "success",
            "offices": ModelOffice().get_all()
            }), 200)

    """
     Fetch a specific political office.
    """
    @office.route('/offices/<int:id>', methods=['GET'])
    def get_specific_office(id):
        office = ModelOffice().get_specific_office(id)
        if office:
            return make_response(jsonify({
                "message": "success",
                "office": office
                }), 200)
        return make_response(jsonify({
            "message": "Office not available"
            }), 204)

    """
     Delete a specific office.
    """
    @office.route('/office/delete/<int:id>', methods=['DELETE'])
    def delete_office(id):
        office = OfficesModel().delete_office(id)
        if office:
            offices.remove(office)
            return make_response(jsonify({
                "message": "office deleted"
                }), 200)
        return make_response(jsonify({
            "message": "That office is not available"
            }), 204)

  