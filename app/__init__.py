from flask import Flask

app = Flask(__name__)

from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)
from app.blueprints.cars import bp as cars_bp
app.register_blueprint(cars_bp)