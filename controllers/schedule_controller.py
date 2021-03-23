from flask import Blueprint, Flask, redirect, render_template, request
from models.schedule import Schedule
import repositories.schedule_repository as schedule_repository
from datetime import date
from datetime import timedelta
import calendar

schedule_blueprint = Blueprint('schedule', __name__)

@schedule_blueprint.route('/schedule')
def rooms():
    schedules = schedule_repository.select_dates()
    schedules_dict = {}
    for i in range(7):
        if schedules[i] is not None:
            schedules_dict['today_schedules_' + str(i)] = schedules[i] 
        else:
            schedules_dict['today_schedules_' + str(i)] = None
    today = date.today()
    today_day = calendar.day_name[today.weekday()]
    today_plus2 = today+timedelta(days=1)
    today_plus2_day = calendar.day_name[today_plus2.weekday()]
    today_plus3 = today+timedelta(days=2)
    today_plus3_day = calendar.day_name[today_plus3.weekday()]
    today_plus4 = today+timedelta(days=3)
    today_plus4_day = calendar.day_name[today_plus4.weekday()]
    today_plus5 = today+timedelta(days=4)
    today_plus5_day = calendar.day_name[today_plus5.weekday()]
    today_plus6 = today+timedelta(days=5)
    today_plus6_day = calendar.day_name[today_plus6.weekday()]
    today_plus7 = today+timedelta(days=6)
    today_plus7_day = calendar.day_name[today_plus7.weekday()]
    
    return render_template('schedule/index.html', schedules=schedules, today=today, today_day=today_day, 
                           today_plus2=today_plus2, today_plus2_day=today_plus2_day, today_plus3=today_plus3, 
                           today_plus3_day=today_plus3_day, today_plus4=today_plus4, today_plus4_day=today_plus4_day, 
                           today_plus5=today_plus5, today_plus5_day=today_plus5_day, today_plus6=today_plus6, 
                           today_plus6_day=today_plus6_day, today_plus7=today_plus7, today_plus7_day=today_plus7_day,
                           today_schedules_0=schedules_dict['today_schedules_0'], today_schedules_1=schedules_dict['today_schedules_1'],
                           today_schedules_2=schedules_dict['today_schedules_2'], today_schedules_3=schedules_dict['today_schedules_3'], 
                           today_schedules_4=schedules_dict['today_schedules_4'], today_schedules_5=schedules_dict['today_schedules_5'], 
                           today_schedules_6=schedules_dict['today_schedules_6'])