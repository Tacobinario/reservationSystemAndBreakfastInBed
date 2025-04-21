from app import create_app

# Crear la aplicación usando la función factory
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
