from flask import Flask
from .extensions import db, migrate
from .config import Config
from .blueprints.category.category_routes import category_bp
from .blueprints.supplier.supplier_routes import supplier_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(category_bp, url_prefix='/api')
    app.register_blueprint(supplier_bp, url_prefix='/api')

    #import models
    from .models import product_category
    from .models import supplier

    return app
