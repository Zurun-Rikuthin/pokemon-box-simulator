from .database import BaseModel
from .extensions import db, Column, Integer, ForeignKey

class CurrentTrainer(db.Model):
    __tablename__ = "currenttrainer"
    trainer_id = db.Column(db.Integer, db.ForeignKey("trainer.id"), primary_key=True)
    caught_pokemon_id = db.Column(db.Integer, db.ForeignKey("caughtpokemon.id"), primary_key=True)

    def __init__(self, trainer_id, caught_pokemon_id):
        if trainer_id is None or caught_pokemon_id is None:
            raise ValueError("Both 'trainer_id' and 'caught_pokemon_id' must be provided.")
        
        self.trainer_id = trainer_id
        self.caught_pokemon_id = caught_pokemon_id

    def __str__(self):
        return f"""
Current Trainer Info:
|   Trainer ID: {self.trainer_id}
|   Caught Pokemon ID: {self.caught_pokemon_id}
"""
