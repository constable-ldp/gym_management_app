from database.run_sql import run_sql
from models.instructor import InstructorSchedule

def save(instructor):
    sql = """INSERT INTO instructor_schedules
             (nickname, monday, tuesday, wednesday, thursday, friday,
              starturday, sunday, start_time, end_time, instructor_id) 
             VALUES ( %s, %s, %s ) 
             RETURNING id"""
    values = [instructor.nickname, instructor.monday, instructor.tuesday,
              instructor.wednesday, instructor.thursday, instructor.friday, 
              instructor.saturday, instructor.sunday, instructor.start_time,
              instructor.end_time, instructor.instructor.id]
    results = run_sql( sql, values )
    instructor.id = results[0]['id']
    return instructor

def select_all():
    instructors = []
    sql = "SELECT * FROM instructor_schedules"
    results = run_sql(sql)
    for row in results:
        instructor = InstructorDetails(row['week_start_date'], row['monday'], 
                                       row['tuesday'], row['wednesday'], 
                                       row['thursday'], row['friday'], 
                                       row['saturday'], row['sunday'],
                                       row['start_time'], row['end_time'],
                                       row['instructor_id'], row['id'])
        instructors.append(instructor)
    return instructors

def update(instructor):
    sql = """UPDATE instructor_schedules
             SET week_start_date = %s, monday = %s, tuesday = %s,
                 wednesday = %s, thursday = %s, friday = %s, saturday = %s,
                 sunday = %s, start_time = %s, end_time = %s, instructor_id = %s
             WHERE id = %s"""
    values = [instructor.week_start_date, instructor.monday, instructor.tuesday, 
              instructor.wednesday, instructor.thursday, instructor.friday,
              instructor.saturday, instructor.sunday, instructor.start_time,
              instructor.end_time, instructor.instructor.id, instructor.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM instructor_schedules"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM instructor_scheudles WHERE id = %s"
    values = [id]
    run_sql(sql, values)