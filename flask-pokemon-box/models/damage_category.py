from .database import BaseModel
from .extensions import db

class DamageCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        if name is None:
            raise ValueError("A 'name' must be provided.")
        
        self.name = name

    def __str__(self): 
        return f"""
Damage Category Info:
|   ID: {self.id}
|   Name: {self.name}            
"""
