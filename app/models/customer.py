from ..extensions import db

class Customer(db.Model):
    __tablename__ = 'customers'
    Customer_id = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(100), nullable=True)
    CustomerFname = db.Column(db.String(50), nullable=False)
    CustomerLname = db.Column(db.String(50), nullable=False)
    Phone = db.Column(db.String(20))
    Email = db.Column(db.String(100))



    def __init__(self, CompanyName, CustomerFname, CustomerLname, Phone, Email):
        self.CompanyName = CompanyName
        self.CustomerFname = CustomerFname
        self.CustomerLname = CustomerLname
        self.Phone = Phone
        self.Email = Email


    def to_dict(self):
        return {
            'Customer_id': self.Customer_id,
            'CompanyName': self.CompanyName,
            'CustomerFname': self.CustomerFname,
            'CustomerLname': self.CustomerLname,
            'Phone': self.Phone,
            'Email': self.Email
        }