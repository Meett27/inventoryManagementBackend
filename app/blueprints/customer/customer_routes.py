from flask import Blueprint, make_response, request, jsonify
from app.extensions import db
from flask_cors import cross_origin
from app.models.customer import Customer

customer_bp = Blueprint('customer', __name__)

# Create a new customer
@customer_bp.route('/createCustomer', methods=['POST'])
@cross_origin(origins="*")
def create_customer():      
    data = request.json
    new_customer = Customer(
        CompanyName=data.get('CompanyName'),
        CustomerFname=data.get('CustomerFname'),
        CustomerLname=data.get('CustomerLname'),
        Phone=data.get('Phone'),
        Email=data.get('Email')
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "Customer created successfully."}), 201


# Get all customers
@customer_bp.route('/getCustomers', methods=['GET'])
@cross_origin(origins="*")
def get_customers():
    customers = Customer.query.all()
    response = jsonify([customer.as_dict() for customer in customers]), 200
    return response 



# Get a specific customer by ID
@customer_bp.route('/getCustomer/<int:customer_id>', methods=['GET'])
@cross_origin(origins="*")
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify(customer.as_dict()), 200 




# Update a customer by ID
@customer_bp.route('/updateCustomer/<int:customer_id>', methods=['PUT'])
@cross_origin(origins="*")
def update_customer(customer_id):        
    customer = Customer.query.get_or_404(customer_id)
    data = request.json
    customer.CompanyName = data.get('CompanyName', customer.CompanyName)
    customer.CustomerFname = data.get('CustomerFname', customer.CustomerFname)
    customer.CustomerLname = data.get('CustomerLname', customer.CustomerLname)
    customer.Phone = data.get('Phone', customer.Phone)
    customer.Email = data.get('Email', customer.Email)
    db.session.commit()
    return jsonify({"message": "Customer updated successfully."}), 200  



# Delete a customer by ID
@customer_bp.route('/deleteCustomer/<int:customer_id>', methods=['DELETE'])
@cross_origin(origins="*")
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted successfully."}), 200  


