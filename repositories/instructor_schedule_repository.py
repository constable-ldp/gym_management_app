from database.run_sql import run_sql
from models.instructor import InstructorSchedule

def save(instructor):
    sql = """INSERT INTO instructor_schedules
             (nickname, monday, tuesday, wednesday, thursday, friday,
              saturday, sunday, start_time, end_time) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ) 
             RETURNING id"""
    values = [instructor.nickname, instructor.monday, instructor.tuesday,
              instructor.wednesday, instructor.thursday, instructor.friday, 
              instructor.saturday, instructor.sunday, instructor.start_time,
              instructor.end_time]
    results = run_sql( sql, values )
    instructor.id = results[0]['id']
    return instructor

def select_all():
    instructors = []
    sql = "SELECT * FROM instructor_schedules"
    results = run_sql(sql)
    for row in results:
        instructor = InstructorSchedule(row['nickname'], row['monday'], 
                                        row['tuesday'], row['wednesday'], 
                                        row['thursday'], row['friday'], 
                                        row['saturday'], row['sunday'],
                                        row['start_time'], row['end_time'], row['id'])
        instructors.append(instructor)
    return instructors

def select(id):
    instructor = None
    sql = "SELECT * FROM instructor_schedules WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        instructor = InstructorSchedule(result['nickname'], result['monday'], 
                                        result['tuesday'], result['wednesday'], 
                                        result['thursday'], result['friday'], 
                                        result['saturday'], result['sunday'],
                                        result['start_time'], result['end_time'],
                                        result['id'])
    return instructor

def update(instructor):
    sql = """UPDATE instructor_schedules
             SET nickname = %s, monday = %s, tuesday = %s,
                 wednesday = %s, thursday = %s, friday = %s, saturday = %s,
                 sunday = %s, start_time = %s, end_time = %s
             WHERE id = %s"""
    values = [instructor.nickname, instructor.monday, instructor.tuesday, 
              instructor.wednesday, instructor.thursday, instructor.friday,
              instructor.saturday, instructor.sunday, instructor.start_time,
              instructor.end_time, instructor.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM instructor_schedules"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM instructor_scheudles WHERE id = %s"
    values = [id]
    run_sql(sql, values)