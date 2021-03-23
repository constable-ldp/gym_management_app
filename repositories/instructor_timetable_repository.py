from database.run_sql import run_sql

from models.instructor import InstructorDetails, InstructorSchedule, InstructorTimetable
import repositories.instructor_details_repository as details_repository
import repositories.instructor_schedule_repository as schedule_repository

def save(timetable):
    sql = """INSERT INTO instructor_timetables ( week_start, i_details_id, i_schedules_id ) 
    VALUES ( %s, %s, %s ) RETURNING id"""
    values = [timetable.week_start_date, timetable.detail.id, timetable.schedule.id]
    results = run_sql( sql, values )
    timetable.id = results[0]['id']
    return timetable


def select_all():
    timetables = []
    sql = "SELECT * FROM instructor_timetables"
    results = run_sql(sql)
    for row in results:
        detail = details_repository.select(row['i_details_id'])
        schedule = schedule_repository.select(row['i_schedules_id'])
        timetable = InstructorTimetable(row['week_start'], detail, schedule, row['id'])
        timetables.append(timetable)
    return timetables

def delete_all():
    sql = "DELETE FROM instructor_timetables"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM instructor_timetables WHERE id = %s"
    values = [id]
    run_sql(sql, values)
