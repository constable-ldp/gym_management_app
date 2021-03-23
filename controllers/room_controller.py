from flask import Blueprint, Flask, redirect, render_template, request
from models.room import Room
import repositories.room_repository as room_repository

rooms_blueprint = Blueprint('rooms', __name__)

@rooms_blueprint.route('/rooms')
def rooms():
    rooms = room_repository.select_all()
    return render_template('rooms/index.html', rooms=rooms)

@rooms_blueprint.route('/rooms/new')
def new_room():
    return render_template('rooms/new.html')

@rooms_blueprint.route('/rooms/new', methods=['POST'])
def add_room():
    name = request.form['name']
    capacity = request.form['capacity']
    description = request.form['description']
    room = Room(name, capacity, description, id)
    room_repository.save(room)
    return redirect('/rooms')

@rooms_blueprint.route('/rooms/<id>')
def see_room(id):
    room = room_repository.select(id)
    return render_template('rooms/edit.html', room=room)


@rooms_blueprint.route('/rooms/<id>', methods=['POST'])
def edit_room(id):
    name = request.form['name']
    capacity = request.form['capacity']
    description = request.form['description']
    room = Room(name, capacity, description, id)
    room_repository.update(room)
    return redirect('/rooms')

@rooms_blueprint.route('/rooms/<id>/delete', methods=['POST'])
def delete_room(id):
    room_repository.delete(id)
    return redirect('/rooms')