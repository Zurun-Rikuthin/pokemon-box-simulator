from .database import BaseModel
from .extensions import db

class Species(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=False, unique=True)
    base_hit_points = db.Column(db.Integer, nullable=False)
    base_attack = db.Column(db.Integer, nullable=False)
    base_defense = db.Column(db.Integer, nullable=False)
    base_special_attack = db.Column(db.Integer, nullable=False)
    base_special_defense = db.Column(db.Integer, nullable=False)
    average_height = db.Column(db.Integer, nullable=False)   # Expects value to be in metres
    average_weight = db.Column(db.Integer, nullable=False)   # Expects value to be in kilograms
    has_alternate_forms = db.Column(db.Boolean, nullable=False)
    types = db.relationship("SpeciesType", backref="species")

    learnable_moves = db.relationship("CanLearn", back_populates="species")

    def __init__(self, params):
        try:
            self.name = params.get("name")
            self.base_hit_points = params.get("baseHp")
            self.base_attack = params.get("baseAtk")
            self.base_defense = params.get("baseDef")
            self.base_special_attack = params.get("baseSpAtk")
            self.base_special_defense = params.get("baseSpDef")
            self.average_height = params.get("avgHeight")
            self.average_weight = params.get("avgWeight")
            self.has_alternate_forms = params.get("hasForms")

        except KeyError as e:
            raise ValueError(
                f"Missing required key: {e}")
        
        except Exception as e:
            raise ValueError(f"Error occurred while initializing {self.__class__.__name__}: {e}")

    def __str__(self):
        return f"""
Pokemon Species Info:
    |- Name: {self.name}
    |- National Pokedex ID: {self.id}
    |- Stats:
    |    |- Base HP : {self.base_hit_points}
    |    |- Base Atk : {self.base_attack}
    |    |- Base Def : {self.base_defense}
    |    |- Base Sp. Atk : {self.base_special_attack}
    |    |- Base Sp. Def : {self.base_special_defense}
    |- Average Height (metres): {self.average_height}
    |- Average Weight (kilograms): {self.average_weight}
    |- Has Alternate Forms: {self.has_alternate_forms}
"""
