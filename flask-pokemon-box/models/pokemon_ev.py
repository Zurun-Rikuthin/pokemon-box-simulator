from .database import BaseModel
from .extensions import db, Column, String, Integer, Boolean, ForeignKey
from .models import Species, SpeciesAbility

class CaughtPokemon(BaseModel):
    __tablename__ = "caughtpokemon"
    id = Column(Integer, primary_key=True)
    species_id = Column(Integer, ForeignKey("species.id"), nullable=False)
    nickname = Column(String(12))
    sex_id = Column(Integer, ForeignKey("sex.id"), nullable=False)

    max_hit_points = Column(Integer, nullable=False)
    current_hit_points = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    special_attack = Column(Integer, nullable=False)
    special_defense = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)

    hit_point_effort_value = Column(Integer, nullable=False)
    attack_effort_value = Column(Integer, nullable=False)
    defense_effort_value = Column(Integer, nullable=False)
    special_attack_effort_value = Column(Integer, nullable=False)
    special_defense_effort_value = Column(Integer, nullable=False)
    speed_effort_value = Column(Integer, nullable=False)

    hit_point_individual_value = Column(Integer, nullable=False)
    attack_individual_value = Column(Integer, nullable=False)
    defense_individual_value = Column(Integer, nullable=False)
    special_attack_individual_value = Column(Integer, nullable=False)
    special_defense_individual_value = Column(Integer, nullable=False)
    speed_individual_value = Column(Integer, nullable=False)

    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    experience_points = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    is_shiny = Column(Boolean, nullable=False)
    nature_id = Column(Integer, ForeignKey("nature.id"), nullable=False)
    has_pokerus = Column(Boolean, nullable=False)
    immune_to_pokerus = Column(Boolean, nullable=False)
    
    alternate_form_id = Column(Integer, ForeignKey("form.id"))
    ability_id = Column(Integer, ForeignKey("ability.id"), nullable=False) 

    def __init__(self, params):
        try:
            species_default = db.session.query(Species).filter_by(species_id=self.species_id).first()
            
            if species_default is not None:
                self.max_hit_points = params.get("max_hit_points", species_default.max_hit_points)
                self.current_hit_points = params.get("current_hit_points", self.max_hit_points)
                self.attack = params.get("attack", species_default.base_attack)
                self.defense = params.get("defense", species_default.base_defense)
                self.special_attack = params.get("special_attack", species_default.base_special_attack)
                self.special_defense = params.get("special_defense", species_default.base_special_defense)
                self.speed = params.get("speed", species_default.base_speed)
                self.height = params.get("height", species_default.average_height)
                self.weight = params.get("weight", species_default.average_weight)

            else:
                raise ValueError("Default values not found for species_id: {}".format(self.species_id))
                 
            self.nickname = params.get("nickname", None)
            self.sex_id = params.get("sex_id")

            self.hit_point_effort_value = params.get("special_attack_effort_values", 0)
            self.attack_effort_value = params.get("attack_effort_values", 0)
            self.defense_effort_value = params.get("defense_effort_values", 0)
            self.special_attack_effort_value = params.get("special_attack_effort_values", 0)
            self.special_defense_effort_value = params.get("special_defense_effort_values", 0)

            self.hit_point_individual_value = params.get("hit_point_individual_value", 0)
            self.attack_individual_value = params.get("attack_individual_value", 0)
            self.defense_individual_value = params.get("defense_individual_value", 0)
            self.special_attack_individual_value = params.get("special_attack_individual_value", 0)
            self.special_defense_individual_value = params.get("special_defense_individual_value", 0)
            self.speed_individual_value = params.get("speed_individual_value", 0)

            self.experience_points = params.get("experience_points", 0)
            self.level = params.get("level", 1)
            self.is_shiny = params.get("is_shiny", False)
            self.nature_id = params.get("nature_id")
            self.has_pokerus = params.get("has_pokerus", False)
            self.immune_to_pokerus = params.get("pokerus_immunity", False)

            self.alternate_form_id = params.get("alternate_form_id", None)
            
            species_abilities = db.session.query(SpeciesAbility).filter_by(
                species_id=self.species_id, ability_id=params.get("ability_id")).first()
            
            if species_abilities is not None:
                self.ability_id = species_abilities.ability_id
            else:
                raise ValueError(f"Provided ability_id is not valid for the given species_id: {self.species_id}")

            

        except KeyError as e:
            raise ValueError(
                f"Missing required key: {e}")
        
        except Exception as e:
            raise ValueError(f"Error occurred while initializing {self.__class__.__name__}: {e}")


    def __str__(self):
        return f"""
Caught Pokemon Info:
|   Personal ID: {self.id}
|   National Pokedex ID: {self.species_id}
|   Nickname: {self.nickname}
|   Sex: {self.sex_id}
|   Stats:
|   |   Base Values
|   |   |   HP: {self.current_hit_points} / {self.max_hit_points}
|   |   |   Attack: {self.attack}
|   |   |   Defense: {self.defense}
|   |   |   Sp. Atk: {self.special_attack}
|   |   |   Sp. Def: {self.special_defense}
|   |   Effort Values:
|   |   |   HP: {self.hit_point_effort_value}
|   |   |   ATK: {self.attack_effort_value}
|   |   |   DEF: {self.defense_effort_value}
|   |   |   Sp. Atk: {self.special_attack_effort_value}
|   |   |   Sp. Def: {self.special_defense_effort_value}
|   |   Individual Values:
|   |   |   HP: {self.hit_point_effort_value}
|   |   |   ATK: {self.attack_effort_value}
|   |   |   DEF: {self.defense_effort_value}
|   |   |   Sp. Atk: {self.special_attack_effort_value}
|   |   |   Sp. Def: {self.special_defense_effort_value}
|   Height (metres): {self.height}
|   Weight (kilograms): {self.weight}
|   Experience Points: {self.experience_points}
|   Level: {self.level}
|   Is Shiny: {self.is_shiny}
|   Nature ID: {self.nature_id}
|   Currently Infected with Pokerus: {self.has_pokerus}
|   Immune to Pokerus: {self.immune_to_pokerus}
|   Alternate Form ID: {self.alternate_form_id}
|   Ability ID: {self.ability_id}
"""
