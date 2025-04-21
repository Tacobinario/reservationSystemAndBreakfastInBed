from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Reservation, db
from .forms import ReservationForm
from flask import flash

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

# ... tus otras rutas ...

@main_routes.route('/edit_reservation/<int:id>', methods=['GET', 'POST'])
def edit_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    form = ReservationForm(obj=reservation)
    
    if form.validate_on_submit():
        reservation.name = form.name.data
        reservation.date = form.date.data
        reservation.time = form.time.data
        reservation.room = form.room.data
        reservation.breakfast_option = form.breakfast_option.data
        
        db.session.commit()
        flash('La reservación ha sido actualizada exitosamente', 'success')

        return redirect(url_for('main.view_reservations'))
    
    return render_template('edit_reservation.html', form=form, reservation=reservation)

@main_routes.route('/delete_reservation/<int:id>')
def delete_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    db.session.delete(reservation)
    db.session.commit()
    flash('La reservación ha sido eliminada exitosamente', 'success')
    return redirect(url_for('main.view_reservations'))