from .database import BaseModel
from .extensions import db, Column, Integer, String, ForeignKey

def Item(BaseModel):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    name = Column(String(12), nullable=False, unique=True)
    item_category_id = Column(Integer, ForeignKey("itemcategory.id"))
    description = Column(String(500), nullable=False, unique=True)

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
