from flask import Flask
from models import db
from controllers.number_controller import bp as number_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

if not app.config['SQLALCHEMY_DATABASE_URI']:
    raise RuntimeError("DATABASE_URL is not set in the environment variables")

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(number_bp)

if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)