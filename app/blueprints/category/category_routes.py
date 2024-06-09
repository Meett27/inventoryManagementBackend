from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.product_category import Category

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

@category_bp.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get_or_404(id)
    return jsonify(category.to_dict())

@category_bp.route('/add_categories', methods=['POST'])
def add_category():
    data = request.get_json()
    new_category = Category(
        name=data['name'],
        description=data.get('description')
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify(new_category.to_dict()), 201

@category_bp.route('/update_category/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get_or_404(id)
    data = request.get_json()
    category.name = data.get('name', category.name)
    category.description = data.get('description', category.description)
    db.session.commit()
    return jsonify(category.to_dict())

@category_bp.route('/delete_category/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return '', 204
