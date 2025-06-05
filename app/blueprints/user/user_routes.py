from flask import Blueprint, make_response, request, jsonify
from app.extensions import db
from flask_cors import cross_origin
from app.models.user import User

user_bp = Blueprint('user', __name__)   


# Create a new user
@user_bp.route('/users', methods=['POST'])
@cross_origin()
def create_user():      
    data = request.json
    new_user = User(
        username=data.get('username'),
        userFName=data.get('userFName'),
        userLName=data.get('userLName'),
        email=data.get('email'),
        password=data.get('password')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully."}), 201


# Get all users
@user_bp.route('/users', methods=['GET'])
@cross_origin()
def get_users():
    users = User.query.all()
    response = jsonify([user.to_dict() for user in users]), 200
    return response 


# Get a single user by ID
@user_bp.route('/users/<int:user_id>', methods=['GET'])
@cross_origin()
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200 



# Update a user by ID
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@cross_origin()
def update_user(user_id):        
    user = User.query.get_or_404(user_id)
    data = request.json
    user.username = data.get('username', user.username)
    user.userFName = data.get('userFName', user.userFName)
    user.userLName = data.get('userLName', user.userLName)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    db.session.commit()
    return jsonify({"message": "User updated successfully."}), 200  



# Delete a user by ID
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@cross_origin()
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully."}), 200      

