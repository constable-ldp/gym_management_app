from flask import Blueprint, Flask, redirect, render_template, request
from models.schedule import Schedule
from models.schedule_member import ScheduleMember
import repositories.schedule_repository as schedule_repository
import repositories.instructor_details_repository as details_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.room_repository as room_repository
import repositories.member_repository as member_repository
from datetime import date
from datetime import timedelta
import calendar

schedule_blueprint = Blueprint('schedule', __name__)

@schedule_blueprint.route('/schedule')
def schedules():
    rooms = room_repository.select_all()
    schedules = schedule_repository.select_dates()
    schedules_dict = {}
    dates = [date.today()+timedelta(days=i) for i in range(7)]
    days = [calendar.day_name[dates[i].weekday()] for i in range(7)]
    for i in range(7):
        if schedules[i] is not None: 
            schedules_dict['today_schedules_' + str(i)] = schedules[i] 
        else:
            schedules_dict['today_schedules_' + str(i)] = None
    return render_template('schedule/index.html', schedules=schedules, dates=dates, 
                            days=days, schedules_dict=schedules_dict, rooms=rooms)

@schedule_blueprint.route('/schedule/new')
def new_schedule():
    instructors = details_repository.select_all()
    classes = gym_class_repository.select_all()
    rooms = room_repository.select_all()
    return render_template('schedule/new.html', instructors=instructors, classes=classes, rooms=rooms)

@schedule_blueprint.route('/schedule/new', methods=['POST'])
def add_schedule():
    class_date = request.form['class_date']
    start_time = request.form['start_time']
    length_mins = request.form['length_mins']
    instructor_id = request.form['instructor_id']
    class_id = request.form['class_id']
    room_id = request.form['room_id']
    instructor = details_repository.select(instructor_id)
    gym_class = gym_class_repository.select(class_id)
    room = room_repository.select(room_id)
    schedule = Schedule(class_date, start_time, length_mins, instructor, gym_class, room, id)
    schedule_repository.save(schedule)
    return redirect('/schedule')

@schedule_blueprint.route('/schedule/<id>')
def show_schedule(id):
    current_cap = schedule_repository.count_member(id)
    schedule = schedule_repository.select(id)
    selected_members = member_repository.selected_members(id)
    return render_template('schedule/show.html', schedule=schedule, members=selected_members, current_cap=current_cap[0][0])

@schedule_blueprint.route('/schedule/<id>/new')
def new_member(id):
    schedule = schedule_repository.select(id)
    members = member_repository.non_selected_members(id)
    return render_template('schedule/new_member.html', schedule=schedule, members=members)

@schedule_blueprint.route('/schedule/<id>/new', methods=['POST'])
def add_member(id):
    member_id = request.form['member_id']
    member = member_repository.select(member_id)
    schedule = schedule_repository.select(id)
    schedule_member = ScheduleMember(member, schedule)
    schedule_repository.save_member(schedule_member)
    return redirect('/schedule')

@schedule_blueprint.route('/schedule/all')
def show_all():
    upcoming_classes = []
    previous_classes = []
    schedules = schedule_repository.select_all()
    for schedule in schedules:
        if schedule.class_date < date.today():
            previous_classes.append(schedule)
        else:
            upcoming_classes.append(schedule)
    return render_template('schedule/all.html', previous_classes=previous_classes, upcoming_classes=upcoming_classes)

@schedule_blueprint.route('/schedule/<id>/remove')
def remove_select_member(id):
    schedule = schedule_repository.select(id)
    members = member_repository.selected_members(id)
    return render_template('schedule/remove_member.html', schedule=schedule, members=members)

@schedule_blueprint.route('/schedule/<id>/remove', methods=['POST'])
def remove_member(id):
    member_id = request.form['member_id']
    schedule_repository.remove_member(id, member_id)
    return redirect('/schedule')