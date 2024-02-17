from .database import BaseModel
from .extensions import db

class Type(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    pokemon = db.relationship("SpeciesType", backref="type")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"""
Elemental Type Info:
    - Name: {self.name}
    - ID: {self.id}
"""
