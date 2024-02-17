# A Pokemon's species determines which moves it can learn.
# When attempting to set/learn a move, if the record cannot be
#   found here, that operation will fail.

from .database import BaseModel
from .extensions import db, Column, Integer, ForeignKey

class CanLearn(BaseModel):
    __table__name = "canlearn"
    move_id = Column(Integer, ForeignKey("move.id"), primary_key=True)
    species_id = Column(Integer, ForeignKey("species.id"), primary_key=True)

    move = db.relationship("Move", back_populates="learnable_by_species")
    species = db.relationship("Species", back_populates="learnable_moves")


    def __init__(self, move_id, species_id):
        if move_id is None or species_id is None:
            raise ValueError("Both 'move_id' and 'species_id' must be provided.")
        
        self.move_id = move_id
        self.species_id = species_id

    def __str__(self):
        return f"""
Learnable Move Info:
|   Ability ID: {self.move_id}
|   Species ID: {self.species_id}
"""
