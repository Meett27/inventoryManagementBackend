from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.role import Role

role_bp = Blueprint('role', __name__)   

# Create a new role
@role_bp.route('/add_roles', methods=['POST'])
def create_role():
    data = request.json
    new_role = Role(
        name=data.get('name'),
        description=data.get('description')
    )
    db.session.add(new_role)
    db.session.commit()
    return jsonify({"message": "Role created successfully."}), 201      

# Get all roles
@role_bp.route('/get_roles', methods=['GET'])
def get_roles():
    roles = Role.query.all()
    return jsonify([role.to_dict() for role in roles]), 200     

# Get a specific role by ID
@role_bp.route('/roles/<int:id>', methods=['GET'])
def get_role(id):
    role = Role.query.get_or_404(id)
    return jsonify(role.to_dict()), 200 

#get role by name
@role_bp.route('/get_role_by_name/<string:name>', methods=['GET'])
def get_role_by_name(name):
    role = Role.query.filter_by(name=name).first_or_404()
    return jsonify(role.to_dict()), 200

# Update a role by ID
@role_bp.route('/update_roles/<int:id>', methods=['PUT'])
def update_role(id):
    role = Role.query.get_or_404(id)
    data = request.json
    role.name = data.get('name', role.name)
    role.description = data.get('description', role.description)
    db.session.commit()
    return jsonify(role.to_dict()), 200

# Delete a role by ID
@role_bp.route('/delete_roles/<int:id>', methods=['DELETE'])
def delete_role(id):
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    return jsonify({"message": "Role deleted successfully."}), 200


