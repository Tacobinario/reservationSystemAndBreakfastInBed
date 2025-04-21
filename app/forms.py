from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ReservationForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    date = DateField('Fecha', validators=[DataRequired()])
    time = TimeField('Hora', validators=[DataRequired()])
    room = StringField('Sala', validators=[DataRequired()])
    breakfast_option = SelectField('Opción de desayuno', choices=[
        ('opcion1', 'Café, pan tostado y fruta'),
        ('opcion2', 'Omelette, jugo de naranja y té'),
        ('opcion3', 'Hotcakes, leche y fruta fresca')
    ])
    submit = SubmitField('Reservar')
