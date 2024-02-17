from .database import BaseModel
from .extensions import db
from sqlalchemy.sql import func

class Trainer(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), unique=True, nullable=False)
    adventure_started_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"""
Elemental Type Info:
    - Name: {self.name}
    - ID: {self.id}
"""
