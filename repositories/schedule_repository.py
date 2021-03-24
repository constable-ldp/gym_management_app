from database.run_sql import run_sql
from models.schedule import Schedule
from models.instructor import InstructorDetails
from models.gym_class import GymClass
from models.room import Room
from models.schedule_member import ScheduleMember
import repositories.instructor_details_repository as instructor_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.room_repository as room_repository
from datetime import timedelta
from datetime import date

def save(schedule):
    sql = """INSERT INTO schedules 
             (class_date, start_time, length_mins, instructor_id, class_id, room_id)
              VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"""
    values = [schedule.class_date, schedule.start_time, schedule.length_mins, schedule.instructor.id,
              schedule.gym_class.id, schedule.room.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    schedule.id = id

def select_all():
    schedules = []
    sql = "SELECT * FROM schedules"
    results = run_sql(sql)
    for row in results:
        instructor = instructor_repository.select(row['instructor_id'])
        gym_class = gym_class_repository.select(row['gym_class_id'])
        room = room_repository.select(row['room_id'])
        schedule = Schedule(row['class_date'], row['length_mins'], row['start_time'], instructor,
                            gym_class, room, row['id'])
        scheules.append(schedule)
    return schedules


def select_dates():
    schedules_list = []
    sql = "SELECT * FROM schedules WHERE class_date = %s ORDER BY start_time"
    for index in range(7):
        schedules = []
        values = [date.today() + timedelta(days=index)]
        results = run_sql(sql, values)
        if results is not None:
            for row in results:
                instructor = instructor_repository.select(row['instructor_id'])
                gym_class = gym_class_repository.select(row['class_id'])
                room = room_repository.select(row['room_id'])
                schedule = Schedule(row['class_date'], row['length_mins'], row['start_time'], instructor,
                                    gym_class, room, row['id'])
                schedules.append(schedule)
        else:
            schedule = None
            schedules.append(schedule)
        schedules_list.append(schedules)
    return schedules_list

def update(schedule):
    sql = """UPDATE schedules 
           SET (class_date, length_mins, start_time, instructor_id, class_id, room_id) = 
           (%s, %s, %s, %s, %s, %s) 
           WHERE id = %s"""
    values = [schedule.class_date, schedule.length_mins, schedule.start_time, schedule.instructor.id,
              schedule.gym_class.id, schedule.room.id]
    run_sql(sql, values)

def select(id):
    schedule = None
    sql = "SELECT * FROM schedules WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        instructor = instructor_repository.select(result['instructor_id'])
        gym_class = gym_class_repository.select(result['class_id'])
        room = room_repository.select(result['room_id'])
        schedule = Schedule(result['class_date'], result['start_time'], result['length_mins'], instructor,
                            gym_class, room, result['id'])
    return schedule

def delete_all():
    sql = "DELETE FROM schedules"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM schedules WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save_member(member):
    sql = """INSERT INTO schedules_members (member_id, schedule_id)
             VALUES (%s, %s)
             RETURNING id"""
    values = [member.member.id, member.schedule.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
