import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.routes import main

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://christinemundi:Nans1247@localhost/ambucare')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'your_secret_key'  # For session management

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    # Import routes and models
    from app import routes, models  # Import models to ensure they are detected

    # Register the main blueprint
    app.register_blueprint(main)

    return app
