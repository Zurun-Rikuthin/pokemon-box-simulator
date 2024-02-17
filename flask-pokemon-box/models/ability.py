from .database import BaseModel
from .extensions import db, Column, Integer, String, Boolean

def Ability(BaseModel):
    __tablename__ = "ability"
    id = Column(Integer, primary_key=True)
    name = Column(String(12), nullable=False, unique=True)
    description = Column(String(500), nullable=False, unique=True)
    is_hidden = Column(Boolean, nullable=False)

    def __init__(self, id, name, description, is_hidden=False):
        if id is None or name is None or description is None:
            raise ValueError("An 'id', 'name' and 'description' must be provided.")
        
        self.id = id
        self.name = name
        self.description = description
        self.is_hidden = is_hidden

    def __str__(self):
        return f"""
Ability Info:
|   ID: {self.id}
|   Name: {self.name}
|   Description: {self.description}
|   Is a Hidden Ability: {self.is_hidden}
"""
