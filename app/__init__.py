from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
<<<<<<< HEAD
from .routes import main as main_blueprint
=======
from .routes import main as main_blueprint 

>>>>>>> 22c33047f11ca6f30b6af4acc44c7249093238af
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        
        app.register_blueprint(main_blueprint)

        db.create_all()

    return app