# If Pokemon has an alternate form with a different ability than
#   its normal form, (e.g., Mega Blastoise [Mega Launcher] vs.
#   Blastoise [Torrent or Rain Dish]), whenever then Pokemon is
#   in that alternate form it will override the normal species' ability/abilities
#   do long as it is in that alternate form.

from .database import BaseModel
from .extensions import db, Column, Integer, ForeignKey

def SpeciesAbility(BaseModel):
    __tablename__ = "availableabilities"
    ability_id = Column(Integer, ForeignKey("ability.id"), primary_key=True)
    species_id = Column(Integer, ForeignKey("species.id"), primary_key=True)

    def __init__(self, ability_id, species_id):
        self.ability_id = ability_id
        self.species_id = species_id

    def __str__(self):
        return f"""
Species Ability Info:
    - Ability ID: {self.ability_id}
    - Species ID: {self.species_id}
"""
