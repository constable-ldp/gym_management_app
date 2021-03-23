class InstructorDetails:

    def __init__(self, first_name, last_name, date_of_birth, id=None) :
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.id = id

class InstructorSchedule:

    def __init__(self, nickname, monday, tuesday, wednesday, thursday, friday, 
                 saturday, sunday, start_time, end_time, instructor, id=None):
        self.nickname = nickname
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.start_time = start_time
        self.end_time = end_time
        self.id = id

class InstructorTimetable:

    def __init__(self, week_start_date, detail, schedule, id=None):
        self.week_start_date = week_start_date
        self.detail = detail
        self.schedule = schedule
        self.id = id