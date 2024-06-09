from flask import Blueprint

product_bp = Blueprint('product', __name__)

from . import routes
from flask import request, jsonify


