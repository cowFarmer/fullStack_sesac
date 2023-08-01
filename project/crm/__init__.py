from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from view.blue_print import register_bp


db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder="static")

    # ORM
    app.instance_path = os.path.join(os.getcwd() + "/model/database")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crm.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # blueprint
    register_bp(app)
    
    return app