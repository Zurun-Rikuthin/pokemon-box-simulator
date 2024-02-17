from .extensions import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base, db.Model):
    __abstract__ = True

    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ", ".join(f"{attr}={getattr(self, attr)!r}" for attr in vars(self))
        return f"{class_name}({attributes})"
    