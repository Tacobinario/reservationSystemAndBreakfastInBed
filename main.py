from app import create_app, db

# Crear la aplicación usando la función factory f
app = create_app()

# Crear un contexto de aplicación y las tablas de la base de datos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
