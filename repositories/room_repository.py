from database.run_sql import run_sql
from models.room import Room

def save(room):
    sql = """INSERT INTO rooms
             (room_name, capacity, description)
             VALUES (%s, %s, %s) 
             RETURNING id"""
    values = [room.room_name, room.capacity, room.description]
    results = run_sql(sql, values)
    print(results)
    room.id = results[0]['id']
    return room

def select_all():
    rooms = []
    sql = "SELECT * FROM rooms"
    results = run_sql(sql)
    for row in results:
        room = Room(row['room_name'], row['capacity'], row['description'], row['id'])
        rooms.append(room)
    return rooms

def select(id):
    room = None
    sql = "SELECT * FROM rooms WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        room = Room(result['room_name'], result['capacity'], result['description'], result['id'])
    return room

def update(room):
    sql = """UPDATE rooms
             SET room_name = %s, capacity = %s, desription = %s
             WHERE id = %s"""
    values = [room.room_name, room.capacity, room.description, room.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM rooms"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM rooms WHERE id = %s"
    values = [id]
    run_sql(sql, values)

