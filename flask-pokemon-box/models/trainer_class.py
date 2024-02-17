from .database import BaseModel
from .extensions import db

class TrainerClass(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __str__(self): 
        return f"""
Trainer Class: {self.name}
    - ID: {self.id}
"""
