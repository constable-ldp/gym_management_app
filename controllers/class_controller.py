from flask import Blueprint, Flask, redirect, render_template, request
from models.gym_class import GymClass
import repositories.gym_class_repository as class_repository

classes_blueprint = Blueprint('classes', __name__)

@classes_blueprint.route('/classes')
def classes():
    classes = class_repository.select_all()
    return render_template('classes/index.html', classes=classes)

@classes_blueprint.route('/classes/new')
def new_class():
    return render_template('classes/new.html')

@classes_blueprint.route('/classes/new', methods=['POST'])
def add_class():
    name = request.form['name']
    description = request.form['description']
    max_time = request.form['max_time']
    capacity = request.form['capacity']
    gym_class = GymClass(name, description, max_time, capacity, id)
    class_repository.save(gym_class)
    return redirect('/classes')

@classes_blueprint.route('/classes/<id>')
def see_class(id):
    gym_class = class_repository.select(id)
    return render_template('classes/edit.html', gym_class=gym_class)


@classes_blueprint.route('/classes/<id>', methods=['POST'])
def edit_class(id):
    name = request.form['name']
    description = request.form['description']
    max_time = request.form['max_time']
    capacity = request.form['capacity']
    gym_class = GymClass(name, description, max_time, capacity, id)
    class_repository.update(gym_class)
    return redirect('/classes')

@classes_blueprint.route('/classes/<id>/delete', methods=['POST'])
def delete_class(id):
    class_repository.delete(id)
    return redirect('/classes')