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
    min_time = request.form['min_time']
    max_time = request.form['max_time']
    min_capacity = request.form['min_capacity']
    max_capacity = request.form['max_capacity']
    gym_class = GymClass(name, description, min_time, max_time, min_capacity, max_capacity, id)
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
    min_time = request.form['min_time']
    max_time = request.form['max_time']
    min_capacity = request.form['min_capacity']
    max_capacity = request.form['max_capacity']
    gym_class = GymClass(name, description, min_time, max_time, min_capacity, max_capacity, id)
    class_repository.update(gym_class)
    return redirect('/classes')