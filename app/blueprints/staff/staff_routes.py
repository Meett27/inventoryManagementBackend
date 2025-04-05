from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.staff import Staff


staff_bp = Blueprint('staff', __name__) 

# Create a new staff member
@staff_bp.route('/add_staff', methods=['POST'])
def create_staff():
    data = request.json
    new_staff = Staff(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        date_of_birth=data.get('date_of_birth'),
        address=data.get('address'),
        email=data.get('email'),
        username=data.get('username'),
        password=data.get('password'),
        role_id=data.get('role_id')
    )
    db.session.add(new_staff)
    db.session.commit()
    return jsonify({"message": "Staff member created successfully."}), 201


# Delete a staff member by ID
@staff_bp.route('/delete_staff/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    db.session.delete(staff)
    db.session.commit()
    return jsonify({"message": "Staff member deleted successfully."}), 200  


# Update a staff member by ID
@staff_bp.route('/update_staff/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    data = request.json
    staff.first_name = data.get('first_name', staff.first_name)
    staff.last_name = data.get('last_name', staff.last_name)
    staff.date_of_birth = data.get('date_of_birth', staff.date_of_birth)
    staff.address = data.get('address', staff.address)
    staff.email = data.get('email', staff.email)
    staff.username = data.get('username', staff.username)
    staff.password = data.get('password', staff.password)
    staff.role_id = data.get('role_id', staff.role_id)
    db.session.commit()
    return jsonify({"message": "Staff member updated successfully."}), 200


    #get all staff members
@staff_bp.route('/get_staff', methods=['GET'])
def get_staff():
    staff = Staff.query.all()
    return jsonify([staff.to_dict() for staff in staff]), 200

#get staff member by ID 
@staff_bp.route('/get_staff/<int:staff_id>', methods=['GET'])
def get_staff_by_id(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    return jsonify(staff.to_dict()), 200


