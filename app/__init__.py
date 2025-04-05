from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate
from .config import Config
from .blueprints.category.category_routes import category_bp
from .blueprints.supplier.supplier_routes import supplier_bp
from .blueprints.product.product_routes import product_bp
from .blueprints.role.role_routes import role_bp
from .blueprints.staff.staff_routes import staff_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    


    # Register Blueprints
    app.register_blueprint(category_bp, url_prefix='/api/category')
    app.register_blueprint(supplier_bp, url_prefix='/api/supplier')
    app.register_blueprint(product_bp, url_prefix='/api/product')
    app.register_blueprint(role_bp, url_prefix='/api/role')
    app.register_blueprint(staff_bp, url_prefix='/api/staff')


    #import models
    from .models import product_category
    from .models import supplier
    from .models import product
    from .models import role
    from .models import staff

    return app
