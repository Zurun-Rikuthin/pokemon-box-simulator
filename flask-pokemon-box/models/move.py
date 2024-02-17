from .database import BaseModel
from .extensions import db, Column, Integer, String, Float, ForeignKey

class Move(BaseModel):
    __tablename__ = "move"
    id = Column(Integer, primary_key=True)
    name = Column(String(12), nullable=False, unique=True)
    description = Column(String(500), nullable=False, unique=True)
    type_id = Column(Integer, ForeignKey("type.id"), nullable=False)
    damage_category_id = Column(Integer, ForeignKey("damagecategory.id"), nullable=False)
    default_power_points = Column(Integer, nullable=False)
    max_power_points = Column(Integer, nullable=False)
    power = Column(Integer)
    accuracy = Column(Integer)
    learnable_by_species = db.relationship("CanLearn", backpopulates="move")

    def __init__(self, name, description, item_category_id = None):
        if name is None or description is None:
            raise ValueError("An 'name', and 'description' must be provided.")
        
        self.id = id
        self.name = name
        self.item_category_id = item_category_id
        self.description = description

    def __str__(self):
        return f"""
Item Info:
|   ID: {self.id}
|   Name: {self.name}
|   Description: {self.description}
|   Item Category ID: {self.item_category_id}
"""
   