from database.run_sql import run_sql
from models.member import Member

def save(member):
    sql = """INSERT INTO members
             (first_name, last_name, email, phone, date_of_birth, 
             membership, premium, member_since, member_until) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
             RETURNING id"""
    values = [member.first_name, member.last_name, member.email, member.phone, member.date_of_birth,
              member.membership, member.premium, member.member_since, member.member_until]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['email'], row['phone'],
                        row['date_of_birth'], row['membership'], row['premium'], 
                        row['member_since'], row['member_until'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['email'], 
                        result['phone'], result['date_of_birth'], result['membership'], 
                        result['premium'], result['member_since'], result['member_until'], 
                        result['id'])
    return member

def update(member):
    sql = """UPDATE members
             SET first_name = %s,
                 last_name = %s,
                 email = %s,
                 phone = %s,
                 date_of_birth = %s,
                 membership = %s,
                 premium = %s,
                 member_since = %s,
                 member_until = %s
             WHERE id = %s"""
    values = [member.first_name, member.last_name, member.email, member.phone, member.date_of_birth,
              member.membership, member.premium, member.member_since, member.member_until,
              member.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def selected_members(id):
    sql = """SELECT members.* FROM members
             INNER JOIN schedules_members ON schedules_members.member_id = members.id
             WHERE schedules_members.schedule_id = %s"""
    values = [id]
    members = run_sql(sql, values)
    return members

def non_selected_members(id):
    sql = """SELECT members.id FROM members
             FULL OUTER JOIN schedules_members ON schedules_members.member_id = members.id
             WHERE schedule_id = %s"""
    values = [id]
    rows = run_sql(sql, values)
    member_ids = tuple([row[0] for row in rows])
    if member_ids == ():
        sql2 = "SELECT * FROM members"
        members = run_sql(sql2)
    else:
        sql2 = """SELECT * FROM members WHERE id NOT IN %s"""
        values2 = [member_ids]
        members = run_sql(sql2, values2)
    return members