from flask import Blueprint

bp = Blueprint('cars', __name__, url_prefix='/my-car-collection')

from app.blueprints.cars import routes