# If Pokemon has an alternate form with a different ability than
#   its normal form, (e.g., Mega Blastoise [Mega Launcher] v.s.
#   Blastoise [Torrent or Rain Dish]), whenever then Pokemon is
#   in that alternate form it will override the normal species' ability/abilities
#   do long as it is in that alternate form.

from .database import BaseModel
from .extensions import db, Column, Integer, ForeignKey


def FormAbility(BaseModel):
    __tablename__ = "formability"
    ability_id = Column(Integer, ForeignKey("ability.id"), primary_key=True)
    form_id = Column(Integer, ForeignKey("form.id"), primary_key=True)

    def __init__(self, ability_id, form_id):
        if ability_id is None or form_id is None:
            raise ValueError("Both 'ability_id' and 'form_id' must be provided.")
        
        self.ability_id = ability_id
        self.form_id = form_id

    def __str__(self):
        return f"""
Form Ability Info:
|    Ability ID: {self.ability_id}
|    Form ID: {self.form_id}
"""
