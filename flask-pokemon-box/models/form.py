from .database import BaseModel
from .extensions import db, Column, Integer, String, ForeignKey

def Form(BaseModel):
    __tablename__ = "form"
    id = Column(Integer, primary_key=True)
    species_id = Column(Integer, ForeignKey(""))

    def __init__(self, ability_id, form_id):
        if ability_id is None or form_id is None:
            raise ValueError("Both 'ability_id' and 'form_id' must be provided.")
        
        self.ability_id = ability_id
        self.form_id = form_id

    def __str__(self):
        return f"""
Form  Info:
|    Ability ID: {self.ability_id}
|    Form ID: {self.form_id}
"""
