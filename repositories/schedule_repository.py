from db.run_sql import run_sql
from models.schedule import Schedule
from models.instructor import InstructorDetails
from models.gym_class import GymClass
from models.room import Room
import repositories.instructor_details_repository as instructor_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.room_repository as room_repository

def save(schedule):
    sql = """INSERT INTO schedules 
             (class_date, length_mins, instructor_id, class_id, room_id)
              VALUES ( %s, %s, %s, %s, %s ) RETURNING id"""
    values = [schedule.class_date, schedule.length_mins, schedule.instructor.id,
              schedule.gym_class.id, schedule.room.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id

def select_all():
    schedules = []
    sql = "SELECT * FROM schedules"
    results = run_sql(sql)
    for row in results:
        instructor = instructor_repository.select(row['instructor_id'])
        gym_class = gym_class_repository.select(row['gym_class_id'])
        room = room_repository.select(row['room_id'])
        schedule = Schedule(row['class_date'], row['length_mins'], instructor,
                            gym_class, room, row['id'])
        scheules.append(schedule)
    return schedules

def update(schedule):
    sql = """UPDATE schedules 
           SET (class_date, length_mins, instructor_id, class_id, room_id) = 
           (%s, %s, %s, %s, %s) 
           WHERE id = %s"""
    values = [schedule.class_date, schedule.length_mins, schedule.instructor.id,
              schedule.gym_class.id, schedule.room.id]
    run_sql(sql, values)

def select(id):
    schedule = None
    sql = "SELECT * FROM schedules WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if schedule is not None:
        instructor = instructor_repository.select(result['instructor_id'])
        gym_class = gym_class_repository.select(result['gym_class_id'])
        room = room_repository.select(result['room_id'])
        schedule = Schedule(result['class_date'], result['length_mins'], instructor,
                            gym_class, room, result['id'])
    return schedule

def delete_all():
    sql = "DELETE FROM schedules"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM schedules WHERE id = %s"
    values = [id]
    run_sql(sql, values)



