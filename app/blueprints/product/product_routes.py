from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.product import Product

product_bp = Blueprint('product', __name__)

# Create a new product
@product_bp.route('/addProducts', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(
        ProductName=data.get('ProductName'),
        ProductDescription=data.get('ProductDescription'),
        SupplierID=data.get('SupplierID'),
        CategoryID=data.get('CategoryID'),
        QuantityPerUnit=data.get('QuantityPerUnit'),
        UnitPrice=data.get('UnitPrice'),
        UnitWeight=data.get('UnitWeight'),
        Size=data.get('Size'),
        Discount=data.get('Discount'),
        UnitsInStock=data.get('UnitsInStock'),
        UnitsonOrder=data.get('UnitsonOrder'),
        ReorderLevel=data.get('ReorderLevel'),
        ProductAvailable=data.get('ProductAvailable', True),
        Note=data.get('Note')
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully."}), 201

# Read all products
@product_bp.route('/getProducts', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.as_dict() for product in products]), 200

# Read a single product by ID
@product_bp.route('/getProduct/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.as_dict()), 200

# Update a product by ID
@product_bp.route('/updateProduct/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.json
    product.ProductName = data.get('ProductName', product.ProductName)
    product.ProductDescription = data.get('ProductDescription', product.ProductDescription)
    product.SupplierID = data.get('SupplierID', product.SupplierID)
    product.CategoryID = data.get('CategoryID', product.CategoryID)
    product.QuantityPerUnit = data.get('QuantityPerUnit', product.QuantityPerUnit)
    product.UnitPrice = data.get('UnitPrice', product.UnitPrice)
    product.UnitWeight = data.get('UnitWeight', product.UnitWeight)
    product.Size = data.get('Size', product.Size)
    product.Discount = data.get('Discount', product.Discount)
    product.UnitsInStock = data.get('UnitsInStock', product.UnitsInStock)
    product.UnitsonOrder = data.get('UnitsonOrder', product.UnitsonOrder)
    product.ReorderLevel = data.get('ReorderLevel', product.ReorderLevel)
    product.ProductAvailable = data.get('ProductAvailable', product.ProductAvailable)
    product.Note = data.get('Note', product.Note)
    db.session.commit()
    return jsonify({"message": "Product updated successfully."}), 200

# Delete a product by ID
@product_bp.route('/deleteProduct/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully."}), 200


