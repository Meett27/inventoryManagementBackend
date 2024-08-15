from ..extensions import db

class Product(db.Model):
    __tablename__ = 'products'
    
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(100), nullable=False)
    ProductDescription = db.Column(db.String(255))
    SupplierID = db.Column(db.Integer, db.ForeignKey('suppliers.SupplierID'), nullable=False)
    CategoryID = db.Column(db.Integer, nullable=False)
    QuantityPerUnit = db.Column(db.String(50))
    UnitPrice = db.Column(db.Float)
    UnitWeight = db.Column(db.Float)
    Size = db.Column(db.String(50))
    Discount = db.Column(db.Float)
    UnitsInStock = db.Column(db.Integer)
    UnitsonOrder = db.Column(db.Integer)
    ReorderLevel = db.Column(db.Integer)
    ProductAvailable = db.Column(db.Boolean, default=True)
    Note = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Product {self.ProductName}>'
    
    def as_dict(self):
        return {
            'ProductID': self.ProductID,
            'ProductName': self.ProductName,
            'ProductDescription': self.ProductDescription,
            'SupplierID': self.SupplierID,
            'CategoryID': self.CategoryID,
            'QuantityPerUnit': self.QuantityPerUnit,
            'UnitPrice': self.UnitPrice,
            'UnitWeight': self.UnitWeight,
            'Size': self.Size,
            'Discount': self.Discount,
            'UnitsInStock': self.UnitsInStock,
            'UnitsonOrder': self.UnitsonOrder,
            'ReorderLevel': self.ReorderLevel,
            'ProductAvailable': self.ProductAvailable,
            'Note': self.Note
        }

