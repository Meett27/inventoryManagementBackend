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
    
    def __repr__(self):
        return f'<Supplier {self.CompanyName}>'