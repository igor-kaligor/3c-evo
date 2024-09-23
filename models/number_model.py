from flask_sqlalchemy import SQLAlchemy
from .base_model import BaseModel, db

class NumberModel(BaseModel):
    """
    Model for phone numbers
    """
    value = db.Column(db.String(20), nullable=False, unique=True)
    monthyPrice = db.Column(db.Float, nullable=False)
    setupPrice = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(5), nullable=False)

