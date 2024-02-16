from app import app
import click, sys
import models
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash


@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    models.db.drop_all()
    models.db.init_app(app)
    models.db.create_all()
    print('database intialized')
    
    testParams = dict(
        name = 'test',
        baseHp = 1,
        baseAtk = 2,
        baseDef = 3,
        baseSpAtk = 4,
        baseSpDef = 5,
        avgHeight = 6,
        avgWeight = 7
    )
    test = models.Species(testParams)
    print(test)