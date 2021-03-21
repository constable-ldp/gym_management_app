from database.run_sql import run_sql
from models.gym_class import GymClass

def save(gym_class):
    sql = """INSERT INTO classes
             (class_name, description, min_time, max_time, min_capacity, max_capacity) 
             VALUES ( %s, %s, %s, %s, %s, %s ) 
             RETURNING id"""
    values = [gym_class.class_name, gym_class.description, gym_class.min_time, 
              gym_class.max_time, gym_class.min_capacity, gym_class.max_capacity]
    results = run_sql( sql, values )
    gym_class.id = results[0]['id']
    return gym_class


def select_all():
    gym_classes = []
    sql = "SELECT * FROM classes"
    results = run_sql(sql)
    for row in results:
        gym_class = GymClass(row['class_name'], row['description'], row['min_time'], 
                             row['max_time'], row['min_capacity'], row['max_capacity'], 
                             row['id'])
        gym_classes.append(gym_class)
    return gym_classes


def select(id):
    gym_class = None
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        gym_class = GymClass(result['name'], result['description'], result['min_time'], \
                   result['max_time'], result['min_capacity'], result['max_capacity'])
    return gym_class


def update(gym_class):
    sql = """UPDATE classes
             SET name = %s,
                 description = %s,
                 min_time = %s,
                 max_time = %s,
                 min_capacity = %s,
                 max_capacity= %s
             WHERE id = %s"""
    values = [gym_class.name, gym_class.description, gym_class.min_time, gym_class.max_time, \
              gym_class.min_capacity, gym_class.max_capacity, gym_class.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)