from database.run_sql import run_sql
from models.instructor import InstructorDetails

def save(instructor):
    sql = """INSERT INTO instructor_details
             (first_name, last_name, date_of_birth) 
             VALUES ( %s, %s, %s ) 
             RETURNING id"""
    values = [instructor.first_name, instructor.last_name, instructor.date_of_birth]
    results = run_sql( sql, values )
    instructor.id = results[0]['id']
    return instructor

def select(id):
    instructor = None
    sql = "SELECT * FROM instructor_details WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        instructor = InstructorDetails(result['first_name'], result['last_name'], 
                                       result['date_of_birth'], result['id'])
    return instructor

def select_all():
    instructors = []
    sql = "SELECT * FROM instructor_details"
    results = run_sql(sql)
    for row in results:
        instructor = InstructorDetails(row['first_name'], row['last_name'], 
                                      row['date_of_birth'], row['id'])
        instructors.append(instructor)
    return instructors

def update(instructor):
    sql = """UPDATE instructor_details
             SET name = %s, last_name = %s, date_of_birth = %s
             WHERE id = %s"""
    values = [instructor.first_name, instructor.last_name, instructor.date_of_birth, instructor.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM instructor_details"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM instructor_details WHERE id = %s"
    values = [id]
    run_sql(sql, values)