from ..extensions import db

class Supplier(db.Model):
    __tablename__ = 'suppliers'
    
    SupplierID = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(100), nullable=False)
    ContactFname = db.Column(db.String(50), nullable=False)
    ContactLname = db.Column(db.String(50), nullable=False)
    ContactTitle = db.Column(db.String(50))
    Address = db.Column(db.String(200))
    Phone = db.Column(db.String(20))
    Fax = db.Column(db.String(20))
    Email = db.Column(db.String(100))
    PaymentMethods = db.Column(db.String(100))
    DiscountType = db.Column(db.String(50))
    
    def to_dict(self):
        return {
            'SupplierID': self.SupplierID,
            'CompanyName': self.CompanyName,
            'ContactFname': self.ContactFname,
            'ContactLname': self.ContactLname,
            'ContactTitle': self.ContactTitle,
            'Address': self.Address,
            'Phone': self.Phone,
            'Fax': self.Fax,
            'Email': self.Email,
            'PaymentMethods': self.PaymentMethods,
            'DiscountType': self.DiscountType
        }