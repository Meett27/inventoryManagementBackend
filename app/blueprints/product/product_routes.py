from flask import Blueprint, make_response, request, jsonify
from app.extensions import db
from flask_cors import cross_origin
from app.models.product import Product

product_bp = Blueprint('product', __name__)

# Create a new product

@product_bp.route('/addProducts', methods=['POST'])
@cross_origin(origins="*")
def create_product():
    data = request.json
    errors = []

    # Helper function to safely cast and validate
    def try_cast(value, cast_type, field_name, required=True, default=None):
        if value is None and not required:
            return default
        try:
            return cast_type(value)
        except (ValueError, TypeError):
            errors.append(f"Invalid {field_name}, must be a {cast_type.__name__}")
            return None

    # Field validations
    product_name = data.get('ProductName')
    if not product_name or not isinstance(product_name, str):
        errors.append('Invalid or missing ProductName')

    product_description = data.get('ProductDescription', '')
    if not isinstance(product_description, str):
        errors.append('Invalid ProductDescription')

    supplier_id = try_cast(data.get('SupplierID'), int, 'SupplierID')
    category_id = try_cast(data.get('CategoryID'), int, 'CategoryID')
    quantity_per_unit = try_cast(data.get('QuantityPerUnit'), int, 'QuantityPerUnit')
    unit_price = try_cast(data.get('UnitPrice'), float, 'UnitPrice')
    unit_weight = try_cast(data.get('UnitWeight'), float, 'UnitWeight')
    discount = try_cast(data.get('Discount', 0.0), float, 'Discount', required=False, default=0.0)
    units_in_stock = try_cast(data.get('UnitsInStock'), int, 'UnitsInStock')
    units_on_order = try_cast(data.get('UnitsonOrder', 0), int, 'UnitsonOrder', required=False, default=0)
    reorder_level = try_cast(data.get('ReorderLevel'), int, 'ReorderLevel')
    size = data.get('Size', None)  # Optional
    note = data.get('Note', '')    # Optional

    product_available = data.get('ProductAvailable', True)
    if not isinstance(product_available, bool):
        errors.append('Invalid ProductAvailable, must be a boolean')

    if errors:
        print("Validation errors:", errors)
        return jsonify({'errors': errors}), 400

    print("Validated data received from frontend:", data)

    # Create product object
    new_product = Product(
        ProductName=product_name,
        ProductDescription=product_description,
        SupplierID=supplier_id,
        CategoryID=category_id,
        QuantityPerUnit=quantity_per_unit,
        UnitPrice=unit_price,
        UnitWeight=unit_weight,
        Size=size,
        Discount=discount,
        UnitsInStock=units_in_stock,
        UnitsonOrder=units_on_order,
        ReorderLevel=reorder_level,
        ProductAvailable=product_available,
        Note=note
    )

    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        print("Database Error:", str(e))
        return jsonify({'error': 'An error occurred while saving the product'}), 500


# Read all products

@product_bp.route('/getProducts', methods=['GET'])
@cross_origin(origins="*") 
def get_products():
    products = Product.query.all()
    response = jsonify([product.as_dict() for product in products]), 200
    return response

# Read a single product by ID
@product_bp.route('/getProduct/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.as_dict()), 200

# Update a product by ID
@product_bp.route('/updateProduct/<int:product_id>', methods=['PUT', 'OPTIONS'])
def update_product(product_id):
    if request.method == 'OPTIONS':
        # Handle preflight CORS request
        response = jsonify({"message": "Preflight OK"})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'PUT,OPTIONS')
        return response, 200
    
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


