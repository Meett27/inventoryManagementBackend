from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.supplier import Supplier

supplier_bp = Blueprint('supplier', __name__)

# Create a new supplier
@supplier_bp.route('/add_suppliers', methods=['POST'])
def create_supplier():
    data = request.json
    new_supplier = Supplier(
        CompanyName=data.get('CompanyName'),
        ContactFname=data.get('ContactFname'),
        ContactLname=data.get('ContactLname'),
        ContactTitle=data.get('ContactTitle'),
        Address=data.get('Address'),
        Phone=data.get('Phone'),
        Fax=data.get('Fax'),
        Email=data.get('Email'),
        PaymentMethods=data.get('PaymentMethods'),
        DiscountType=data.get('DiscountType')
    )
    db.session.add(new_supplier)
    db.session.commit()
    return jsonify({"message": "Supplier created successfully."}), 201

# Read all suppliers
@supplier_bp.route('/getSuppliers', methods=['GET'])
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([supplier.as_dict() for supplier in suppliers]), 200

# Read a single supplier by ID
@supplier_bp.route('/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    return jsonify(supplier.as_dict()), 200

# Update a supplier by ID
@supplier_bp.route('/update_suppliers/<int:supplier_id>', methods=['PUT'])
def update_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    data = request.json
    supplier.CompanyName = data.get('CompanyName', supplier.CompanyName)
    supplier.ContactFname = data.get('ContactFname', supplier.ContactFname)
    supplier.ContactLname = data.get('ContactLname', supplier.ContactLname)
    supplier.ContactTitle = data.get('ContactTitle', supplier.ContactTitle)
    supplier.Address = data.get('Address', supplier.Address)
    supplier.Phone = data.get('Phone', supplier.Phone)
    supplier.Fax = data.get('Fax', supplier.Fax)
    supplier.Email = data.get('Email', supplier.Email)
    supplier.PaymentMethods = data.get('PaymentMethods', supplier.PaymentMethods)
    supplier.DiscountType = data.get('DiscountType', supplier.DiscountType)
    db.session.commit()
    return jsonify({"message": "Supplier updated successfully."}), 200

# Delete a supplier by ID
@supplier_bp.route('/suppliers/<int:supplier_id>', methods=['DELETE'])
def delete_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    db.session.delete(supplier)
    db.session.commit()
    return jsonify({"message": "Supplier deleted successfully."}), 200

# Utility method to convert Supplier object to dict
def supplier_as_dict(supplier):
    return {
        'SupplierID': supplier.SupplierID,
        'CompanyName': supplier.CompanyName,
        'ContactFname': supplier.ContactFname,
        'ContactLname': supplier.ContactLname,
        'ContactTitle': supplier.ContactTitle,
        'Address': supplier.Address,
        'Phone': supplier.Phone,
        'Fax': supplier.Fax,
        'Email': supplier.Email,
        'PaymentMethods': supplier.PaymentMethods,
        'DiscountType': supplier.DiscountType
    }

Supplier.as_dict = supplier_as_dict
