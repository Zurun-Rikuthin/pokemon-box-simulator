from .database import BaseModel
from .extensions import db

class SpeciesType(db.Model):
    species_id = db.Column(db.Integer, db.ForeignKey("species.id"), primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey("type.id"), primary_key=True)

    def __init__(self, params):
        try:
            self.species_id = params.get("species_id")
            self.type_id = params.get("type_id")

        except KeyError as e:
            raise ValueError(
                f"Missing required key: {e}")
        
        except Exception as e:
            raise ValueError(f"Error occurred while initializing {self.__class__.__name__}: {e}")

    def __str__(self):
        return f"""
Pokemon Species Type Info:
    - National Pokedex ID: {self.species_id}
    - Type ID: {self.type_id}
"""
