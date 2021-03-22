class Schedule:

    def __init__(self, class_date, length_mins, instructor, gym_class, room, id=None):
        self.class_date = class_date
        self.length_mins = length_mins
        self.instructor = instructor
        self.gym_class = gym_class
        self.room = room
        self.id = id