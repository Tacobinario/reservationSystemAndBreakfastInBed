from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializar la base de datos
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurar la clave secreta y la base de datos
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'

    # Inicializar extensiones
    db.init_app(app)

    # Registrar las rutas principales
    from .routes import main_routes
    app.register_blueprint(main_routes)

    return app
