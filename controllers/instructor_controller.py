from flask import Blueprint, Flask, redirect, render_template, request
from models.instructor import InstructorTimetable, InstructorDetails, InstructorSchedule
import repositories.instructor_timetable_repository as timetable_repository
import repositories.instructor_details_repository as details_repository
import repositories.instructor_schedule_repository as schedule_repository

instructors_blueprint = Blueprint('instructors', __name__)

@instructors_blueprint.route('/instructors')
def instructors():
    instructors = timetable_repository.select_all()
    return render_template('instructor/index.html', instructors=instructors)

@instructors_blueprint.route('/instructors/new_instructor')
def show_instructor():
    return render_template('instructor/new_dets.html')


@instructors_blueprint.route('/instructors/new_instructor', methods=['POST'])
def new_instructor():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    instructor = InstructorDetails(first_name, last_name, date_of_birth, id)   
    details_repository.save(instructor)
    return redirect('/instructors')

@instructors_blueprint.route('/instructors/new_schedule')
def show_schedule():
    return render_template('instructor/new_sch.html')


@instructors_blueprint.route('/instructors/new_schedule', methods=['POST'])
def new_scheudle():
    nickname = request.form['nickname']
    variables = [False] * 7
    strings = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for index in range(len(variables)):
        if request.form.get(strings[index]):
            variables[index] = True
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    instructor = InstructorSchedule(nickname, variables[0], variables[1], variables[2], variables[3],
                                    variables[4], variables[5], variables[6], start_time, end_time, id)   
    schedule_repository.save(instructor)
    return redirect('/instructors')

@instructors_blueprint.route('/instructors/new_timetable')
def show_timetable():
    instructors = details_repository.select_all()
    schedules = schedule_repository.select_all()
    return render_template('instructor/new_tim.html', instructors=instructors, schedules=schedules)

@instructors_blueprint.route('/instructors/new_timetable', methods=['POST'])
def add_timetable():
    instructor_id = request.form['instructor_id']
    schedule_id = request.form['schedule_id']
    start_date = request.form['start_date']
    instructor = details_repository.select(instructor_id)
    schedule = schedule_repository.select(schedule_id)
    timetable = InstructorTimetable(start_date, instructor, schedule, id)
    timetable_repository.save(timetable)
    return redirect('/instructors')

@instructors_blueprint.route('/instructors/schedule/<id>')
def e_schedule(id):
    schedule = schedule_repository.select(id)
    return render_template('instructor/edit_sch.html', schedule=schedule)

@instructors_blueprint.route('/instructors/schedule/<id>', methods=['POST'])
def edit_schedule(id):
    nickname = request.form['name']
    variables = [False] * 7
    strings = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for index in range(len(variables)):
        if request.form.get(strings[index]):
            variables[index] = True
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    instructor = InstructorSchedule(nickname, variables[0], variables[1], variables[2], variables[3],
                                    variables[4], variables[5], variables[6], start_time, end_time, id)   
    schedule_repository.update(instructor)
    return redirect('/instructors')

@instructors_blueprint.route('/instructors/details/<id>')
def e_details(id):
    details = details_repository.select(id)
    return render_template('instructor/edit_dets.html', details=details)

@instructors_blueprint.route('/instructors/details/<id>', methods=['POST'])
def edit_details(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    instructor = InstructorDetails(first_name, last_name, date_of_birth, id)   
    details_repository.update(instructor)
    return redirect('/instructors')