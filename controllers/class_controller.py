from flask import Blueprint, Flask, redirect, render_template, request
from models.gym_class import GymClass
import repositories.gym_class_repository as class_repository

classes_blueprint = Blueprint('classes', __name__)

@classes_blueprint.route('/classes')
def classes():
    classes = class_repository.select_all()
    return render_template('classes/index.html', classes=classes)