from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

db = SQLAlchemy(app)


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    baseHp = db.Column(db.Integer, nullable=False)
    baseDef = db.Column(db.Integer, nullable=False)
    baseAtk = db.Column(db.Integer, nullable=False)
    baseDef = db.Column(db.Integer, nullable=False)
    baseSpAtk = db.Column(db.Integer, nullable=False)
    baseSpDef = db.Column(db.Integer, nullable=False)
    avgHeight = db.Column(db.Integer, nullable=False)
    avgWeight = db.Column(db.Integer, nullable=False)

    def __init__(self, params):
        self.name = params.get('name')
        self.baseHp = params.get('baseHp')
        self.baseAtk = params.get('baseAtk')
        self.baseDef = params.get('baseDef')
        self.baseSpAtk = params.get('baseSpAtk')
        self.baseSpDef = params.get('baseSpDef')
        self.avgHeight = params.get('avgHeight')
        self.avgWeight = params.get('avgWeight')
    
    def __repr__(self):
        return f"""
{self.__class__.__name__}({{
    'name' : '{self.name}',
    'baseHp' = {self.baseHp},
    'baseAtk' = {self.baseAtk},
    'baseDef' = {self.baseDef},
    'baseSpAtk' = {self.baseSpAtk},
    'baseSpDef' = {self.baseSpDef},
    'avgHeight' = {self.avgHeight},
    'avgWeight' = {self.avgWeight}
}})
"""


class PokemonType(db.Model):
    speciesId = db.Column(db.Integer, db.ForeignKey('species.id'),
                          primary_key=True)
    typeId = db.Column(db.Integer, db.ForeignKey('type.id'),
                          primary_key=True)
    
    def __init__(self, speciesId, typeId):
        self.speciesId = speciesId
        self.typeId = typeId


class Sex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class CaughtPokemon(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('species.id'),
                   primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    sexId = db.Column(db.Boolean, db.ForeignKey('sex.id'))
    baseHp = db.Column(db.Integer, nullable=False)
    baseDef = db.Column(db.Integer, nullable=False)
    baseAtk = db.Column(db.Integer, nullable=False)
    baseDef = db.Column(db.Integer, nullable=False)
    baseSpAtk = db.Column(db.Integer, nullable=False)
    baseSpDef = db.Column(db.Integer, nullable=False)
    avgHeight = db.Column(db.Integer, nullable=False)
    avgWeight = db.Column(db.Integer, nullable=False)

    def __init__(self, params):
        self.name = params.get('name')
        self.sexId = params.get('sexId')
        self.baseHp = params.get('baseHp')
        self.baseAtk = params.get('baseAtk')
        self.baseDef = params.get('baseDef')
        self.baseSpAtk = params.get('baseSpAtk')
        self.baseSpDef = params.get('baseSpDef')
        self.avgHeight = params.get('avgHeight')
        self.avgWeight = params.get('avgWeight')


class Trainer(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('species.id'),
                   primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    genderId = db.Column(db.Boolean, db.ForeignKey('gender.id'))
    money = db.Column(db.Integer, nullable=False)

    def __init__(self, name, genderId, money):
        self.name = name
        self.genderId = genderId
        self.money = money


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainerId = db.Column(db.Integer, db.ForeignKey('trainer.id'),
                   unique=True, nullable=False)

    def __init__(self, trainerId):
        self.trainerId = trainerId


class TeamMembers(db.Model):
    teamId = db.Column(db.Integer, db.ForeignKey('team.id'),
                   primary_key=True)
    memberId = db.Column(db.Integer, db.ForeignKey('caughtpokemon.id'),
                   primary_key=True)
    
    def __init__(self, teamId, memberId):
        self.teamId = teamId
        self.memberId = memberId





"""
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func

db = SQLAlchemy(app)


class Abilities(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class CurrentOwner(db.Model):
    __tablename__ = 'current_owner'
    trainer_id = db.Column(db.Integer, primary_key=True)
    caught_pokemon_id = db.Column(db.Integer,
                                  db.ForeignKey('caughtpokemon.id'),
                                  primary_key=True)


class CaughtPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species_id = db.Column(db.Integer,
                           db.ForeignKey('species.id'),
                           nullable=False)
    nickname = db.Column(db.String(100))
    sex_id = db.Column(db.Integer, db.ForeignKey('sex.id'), nullable=False)
    max_hp = db.Column(db.Integer, nullable=False)
    max_atk = db.Column(db.Integer, nullable=False)
    max_def = db.Column(db.Integer, nullable=False)
    max_sp_atk = db.Column(db.Integer, nullable=False)
    max_sp_def = db.Column(db.Integer, nullable=False)
    curr_hp = db.Column(db.Integer, nullable=False)
    curr_atk = db.Column(db.Integer, nullable=False)
    curr_def = db.Column(db.Integer, nullable=False)
    curr_sp_atk = db.Column(db.Integer, nullable=False)
    curr_sp_def = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    exp = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    held_item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    is_shiny = db.Column(db.Boolean, nullable=False)
    curr_form_id = db.Column(db.Integer, db.ForeignKey('forms.id'))


class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)


class OriginalOwner(db.Model):
    __tablename__ = 'original_owner'
    trainer_id = db.Column(db.Integer, primary_key=True)
    caught_pokemon_id = db.Column(db.Integer,
                                  db.ForeignKey('caught_pokemon.id'),
                                  primary_key=True)


class Sex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer,
                           db.ForeignKey('trainer.id'),
                           unique=True)


class TeamMembers(db.Model):
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True)
    caught_pokemon_id = db.Column(db.Integer,
                                  db.ForeignKey('caughtpokemon.id'),
                                  primary_key=True)


class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    adventure_start_date = db.Column(db.Date, nullable=False)
    adventure_start_time = db.Column(db.Time, nullable=False)
    money = db.column(db.Integer, nullable=False)
    gender = db.column(db.Integer, db.ForeignKey('gender.id'))
    trainer_class_id = db.Column(db.Integer, db.ForeignKey('trainer_class.id'))


class TrainerClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)

"""