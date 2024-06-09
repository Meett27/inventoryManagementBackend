from flask import Flask
from .extensions import db, migrate
from .config import Config
from .blueprints.category.category_routes import category_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(category_bp, url_prefix='/api')

    #import models
    from .models import product_category

    return app
