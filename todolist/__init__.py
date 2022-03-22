from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

db = SQLAlchemy()

def create_app():
    app = Flask("todolist")
    app.config.from_object(DevConfig)
    db.init_app(app)

    with app.app_context():
        from todolist import routes
        db.create_all()

    return app