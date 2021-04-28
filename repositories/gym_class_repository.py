from database.run_sql import run_sql
from models.gym_class import GymClass

def save(gym_class):
    sql = """INSERT INTO classes
             (class_name, description, max_time, capacity) 
             VALUES ( %s, %s, %s, %s ) 
             RETURNING id"""
    values = [gym_class.class_name, gym_class.description, gym_class.max_time, gym_class.capacity]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    gym_classes = []
    sql = "SELECT * FROM classes ORDER BY id"
    results = run_sql(sql)
    for row in results:
        gym_class = GymClass(row['class_name'], row['description'], row['max_time'], 
                             row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def select(id):
    gym_class = None
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        gym_class = GymClass(result['class_name'], result['description'], result['max_time'],
                             result['capacity'], result['id'])
    return gym_class

def update(gym_class):
    sql = """UPDATE classes
             SET class_name = %s,
                 description = %s,
                 max_time = %s,
                 capacity = %s
             WHERE id = %s"""
    values = [gym_class.class_name, gym_class.description, gym_class.max_time,
              gym_class.capacity, gym_class.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)