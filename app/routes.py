from flask import Blueprint, render_template, request, redirect, url_for
from .models import Reservation, db
from .forms import ReservationForm

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/reservations', methods=['GET', 'POST'])
def reservations():
    form = ReservationForm()
    if form.validate_on_submit():
        new_reservation = Reservation(
            name=form.name.data,
            date=form.date.data,
            time=form.time.data,
            room=form.room.data,
            breakfast_option=form.breakfast_option.data
        )
        db.session.add(new_reservation)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('reservation.html', form=form)

@main_routes.route('/view_reservations')
def view_reservations():
    reservations = Reservation.query.all()
    return render_template('view_reservations.html', reservations=reservations)
