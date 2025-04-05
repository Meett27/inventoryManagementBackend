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
    # Gatekeeping: Validate each field and assign default values if necessary
    
    product_name = data.get('ProductName')
    if not product_name or not isinstance(product_name, str):
        return jsonify({'error': 'Invalid or missing ProductName'}), 400

    product_description = data.get('ProductDescription', '')  # Default empty string if missing
    if not isinstance(product_description, str):
        return jsonify({'error': 'Invalid ProductDescription'}), 400

    supplier_id = data.get('SupplierID')
    try:
        supplier_id = int(supplier_id)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid SupplierID, must be an integer'}), 400

    category_id = data.get('CategoryID')
    try:
        category_id = int(category_id)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid CategoryID, must be an integer'}), 400

    quantity_per_unit = data.get('QuantityPerUnit')
    try:
        quantity_per_unit = int(quantity_per_unit)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid QuantityPerUnit, must be an integer'}), 400

    unit_price = data.get('UnitPrice')
    try:
        unit_price = float(unit_price)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid UnitPrice, must be a float'}), 400

    unit_weight = data.get('UnitWeight')
    try:
        unit_weight = float(unit_weight)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid UnitWeight, must be a float'}), 400

    size = data.get('Size', None)  # Nullable field

    discount = data.get('Discount', 0.0)  # Default to 0.0 if not provided
    try:
        discount = float(discount)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid Discount, must be a float'}), 400

    units_in_stock = data.get('UnitsInStock')
    try:
        units_in_stock = int(units_in_stock)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid UnitsInStock, must be an integer'}), 400

    units_on_order = data.get('UnitsonOrder', 0)  # Default to 0 if not provided
    try:
        units_on_order = int(units_on_order)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid UnitsonOrder, must be an integer'}), 400

    reorder_level = data.get('ReorderLevel')
    try:
        reorder_level = int(reorder_level)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid ReorderLevel, must be an integer'}), 400

    product_available = data.get('ProductAvailable', True)  # Default to True if not provided
    if not isinstance(product_available, bool):
        return jsonify({'error': 'Invalid ProductAvailable, must be a boolean'}), 400

    note = data.get('Note', '')  # Optional field, default to empty string
    
    print(data, "This is coming from the frontend")

    # Now create the product after validation
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

    # Add product to database
    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
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


