from flask import Flask
from extensions import db
import models

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("Created database")
    
    return app

app = create_app()
