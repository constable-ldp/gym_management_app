class GymClass:

    def __init__(self, class_name, description, min_time, max_time, 
                 min_capacity, max_capacity, id=None):
        self.class_name = class_name
        self.description = description
        self.min_time = min_time
        self.max_time = max_time
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity
        self.id = id