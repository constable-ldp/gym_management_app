from flask import Blueprint, Flask, redirect, render_template, request
from models.instructor import InstructorTimetable, InstructorDetails, InstructorSchedule
import repositories.instructor_timetable_repository as timetable_repository
import repositories.instructor_details_repository as details_repository
import repositories.instructor_schedule_repository as schedule_repository

instructors_blueprint = Blueprint('instructors', __name__)

@instructors_blueprint.route('/instructors')
def instructors():
    instructors = timetable_repository.select_all()
    return render_template('instructor/index.html', instructors = instructors)