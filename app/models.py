from . import db

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    room = db.Column(db.String(50), nullable=False)
    breakfast_option = db.Column(db.String(50), nullable=False)  # Opción de desayuno
