from models.gym_class import GymClass
from models.member import Member
from models.room import Room
from models.instructor import InstructorDetails, InstructorSchedule, InstructorTimetable
from models.schedule import Schedule
import repositories.gym_class_repository as class_repository
import repositories.member_repository as member_repository
import repositories.room_repository as room_repository
import repositories.instructor_timetable_repository as timetable_repository
import repositories.instructor_details_repository as details_repository
import repositories.instructor_schedule_repository as i_schedule_repository
import repositories.schedule_repository as schedule_repository
import datetime

class_1 = GymClass('Hot Yoga', 
                   'Vigorous form of yoga performed in a very warm studio', 
                    60, 16)
class_2 = GymClass('CrossFit', 'Bodyweight workout', 90, 24)

class_repository.save(class_1)
class_repository.save(class_2)

member_1 = Member('John', 'Smith', 'johnsmith@gmail.com', '07595964019', 
                 datetime.date(1997, 5, 17), True, False, datetime.date(2021, 3, 21),
                 datetime.date(2021, 4, 21))
member_repository.save(member_1)

room1 = Room('Room 1', 24, 'Large Room')
instructor_dets = InstructorDetails('Mary', 'Jones', datetime.date(1992, 3, 12))
instructor_sch = InstructorSchedule('9-5', True, True, True, 
                                             True, True, False, False, datetime.time(9, 0), 
                                             datetime.time(17, 0))
instructor_tim = InstructorTimetable(datetime.date(2021, 3, 21), instructor_dets, instructor_sch)

room_repository.save(room1)
details_repository.save(instructor_dets)
i_schedule_repository.save(instructor_sch)
timetable_repository.save(instructor_tim)

schedule_1 = Schedule(datetime.date(2021, 3, 24), datetime.time(11,0), 45, instructor_dets, class_1, room1)
schedule_repository.save(schedule_1)
