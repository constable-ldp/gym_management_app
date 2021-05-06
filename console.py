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

class_1 = GymClass('Hot Yoga', 'Yoga in a very warm studio', 60, 16)
class_2 = GymClass('CrossFit', 'Bodyweight workout', 90, 24)
class_3 = GymClass('Spinning', 'Stationary indoor cycling', 60, 20)
class_4 = GymClass('Adult Swimming Lessons', 'Adult Swimming Lessons', 60, 20)
class_5 = GymClass('Water Aerobics', 'Water Exercises', 60, 25)

class_repository.save(class_1)
class_repository.save(class_2)
class_repository.save(class_3)
class_repository.save(class_4)
class_repository.save(class_5)

member_1 = Member('John', 'Smith', 'johnsmith@gmail.com', '07595964019', 
                 datetime.date(1997, 5, 17), True, False, datetime.date(2021, 3, 21),
                 datetime.date(2022, 3, 21))
member_2 = Member('Luke', 'Jones', 'lukejones@gmail.com', '07595964018', 
                  datetime.date(1992, 1, 15), False, False, None, None)
member_3 = Member('Mary', 'Taylor', 'marytaylor@gmail.com', '07595964048', 
                  datetime.date(1988, 12, 1), True, True, datetime.date(2021, 4, 15),
                  datetime.date(2022, 7, 15))
member_4 = Member('Susan', 'Wilson', 'susanwilson@gmail.com', '07595964013', 
                  datetime.date(1968, 12, 1), False, False, None, None)

member_repository.save(member_1)
member_repository.save(member_2)
member_repository.save(member_3)
member_repository.save(member_4)

room_1 = Room('Studio 1', 24, 'Large Room')
room_2 = Room('Studio 2', 4, 'Small Room')
room_3 = Room('Swimming Pool', 50, 'Pool')

room_repository.save(room_1)
room_repository.save(room_2)
room_repository.save(room_3)


instructor_dets_1 = InstructorDetails('Mary', 'Johnson', datetime.date(1992, 3, 12))
instructor_dets_2 = InstructorDetails('Zach', 'Smith', datetime.date(1990, 8, 14))
instructor_dets_3 = InstructorDetails('John', 'Wilson', datetime.date(1990, 8, 14))


# instructor_sch = InstructorSchedule('9-5', True, True, True, 
#                                              True, True, False, False, datetime.time(9, 0), 
#                                              datetime.time(17, 0))
# instructor_tim = InstructorTimetable(datetime.date(2021, 3, 21), instructor_dets, instructor_sch)


details_repository.save(instructor_dets_1)
details_repository.save(instructor_dets_2)
details_repository.save(instructor_dets_3)
# i_schedule_repository.save(instructor_sch)
# timetable_repository.save(instructor_tim)

schedule_1 = Schedule(datetime.date(2021, 5, 3), datetime.time(10, 0), 60, instructor_dets_1, class_1, room_1)
schedule_2 = Schedule(datetime.date(2021, 5, 3), datetime.time(13, 0), 60, instructor_dets_1, class_1, room_1)
schedule_3 = Schedule(datetime.date(2021, 5, 3), datetime.time(16, 0), 60, instructor_dets_1, class_1, room_1)
schedule_4 = Schedule(datetime.date(2021, 5, 5), datetime.time(10, 0), 60, instructor_dets_1, class_1, room_1)
schedule_5 = Schedule(datetime.date(2021, 5, 5), datetime.time(13, 0), 60, instructor_dets_1, class_1, room_1)
schedule_6 = Schedule(datetime.date(2021, 5, 5), datetime.time(16, 0), 60, instructor_dets_1, class_1, room_1)
schedule_7 = Schedule(datetime.date(2021, 5, 7), datetime.time(10, 0), 60, instructor_dets_1, class_1, room_1)
schedule_8 = Schedule(datetime.date(2021, 5, 7), datetime.time(13, 0), 60, instructor_dets_1, class_1, room_1)
schedule_9 = Schedule(datetime.date(2021, 5, 7), datetime.time(16, 0), 60, instructor_dets_1, class_1, room_1)
schedule_10 = Schedule(datetime.date(2021, 5, 4), datetime.time(11, 0), 60, instructor_dets_1, class_3, room_2)
schedule_11 = Schedule(datetime.date(2021, 5, 4), datetime.time(14, 0), 60, instructor_dets_1, class_3, room_2)
schedule_12 = Schedule(datetime.date(2021, 5, 6), datetime.time(11, 0), 60, instructor_dets_1, class_3, room_2)
schedule_13 = Schedule(datetime.date(2021, 5, 6), datetime.time(14, 0), 60, instructor_dets_1, class_3, room_2)

schedule_14 = Schedule(datetime.date(2021, 5, 3), datetime.time(9, 0), 60, instructor_dets_2, class_2, room_2)
schedule_15 = Schedule(datetime.date(2021, 5, 3), datetime.time(12, 0), 60, instructor_dets_2, class_2, room_2)
schedule_16 = Schedule(datetime.date(2021, 5, 3), datetime.time(15, 0), 60, instructor_dets_2, class_2, room_2)
schedule_17 = Schedule(datetime.date(2021, 5, 5), datetime.time(9, 0), 60, instructor_dets_2, class_2, room_2)
schedule_18 = Schedule(datetime.date(2021, 5, 5), datetime.time(12, 0), 60, instructor_dets_2, class_2, room_2)
schedule_19 = Schedule(datetime.date(2021, 5, 5), datetime.time(15, 0), 60, instructor_dets_2, class_2, room_2)
schedule_20 = Schedule(datetime.date(2021, 5, 7), datetime.time(9, 0), 60, instructor_dets_2, class_2, room_2)
schedule_21 = Schedule(datetime.date(2021, 5, 7), datetime.time(12, 0), 60, instructor_dets_2, class_2, room_2)
schedule_22 = Schedule(datetime.date(2021, 5, 7), datetime.time(15, 0), 60, instructor_dets_2, class_2, room_2)
schedule_23 = Schedule(datetime.date(2021, 5, 4), datetime.time(8, 0), 60, instructor_dets_2, class_4, room_3)
schedule_24 = Schedule(datetime.date(2021, 5, 4), datetime.time(12, 0), 60, instructor_dets_2, class_4, room_3)
schedule_25 = Schedule(datetime.date(2021, 5, 6), datetime.time(8, 0), 60, instructor_dets_2, class_4, room_3)
schedule_26 = Schedule(datetime.date(2021, 5, 6), datetime.time(12, 0), 60, instructor_dets_2, class_4, room_3)

schedule_27 = Schedule(datetime.date(2021, 5, 3), datetime.time(15, 0), 60, instructor_dets_3, class_5, room_3)
schedule_28 = Schedule(datetime.date(2021, 5, 3), datetime.time(18, 0), 60, instructor_dets_3, class_5, room_3)
schedule_29 = Schedule(datetime.date(2021, 5, 5), datetime.time(15, 0), 60, instructor_dets_3, class_5, room_3)
schedule_30 = Schedule(datetime.date(2021, 5, 5), datetime.time(18, 0), 60, instructor_dets_3, class_5, room_3)
schedule_31 = Schedule(datetime.date(2021, 5, 7), datetime.time(15, 0), 60, instructor_dets_3, class_5, room_3)
schedule_32 = Schedule(datetime.date(2021, 5, 7), datetime.time(18, 0), 60, instructor_dets_3, class_5, room_3)

schedule_repository.save(schedule_1)
schedule_repository.save(schedule_2)
schedule_repository.save(schedule_3)
schedule_repository.save(schedule_4)
schedule_repository.save(schedule_5)
schedule_repository.save(schedule_6)
schedule_repository.save(schedule_7)
schedule_repository.save(schedule_8)
schedule_repository.save(schedule_9)
schedule_repository.save(schedule_10)
schedule_repository.save(schedule_11)
schedule_repository.save(schedule_12)
schedule_repository.save(schedule_13)
schedule_repository.save(schedule_14)
schedule_repository.save(schedule_15)
schedule_repository.save(schedule_16)
schedule_repository.save(schedule_17)
schedule_repository.save(schedule_18)
schedule_repository.save(schedule_19)
schedule_repository.save(schedule_20)
schedule_repository.save(schedule_21)
schedule_repository.save(schedule_22)
schedule_repository.save(schedule_23)
schedule_repository.save(schedule_24)
schedule_repository.save(schedule_25)
schedule_repository.save(schedule_26)
schedule_repository.save(schedule_27)
schedule_repository.save(schedule_28)
schedule_repository.save(schedule_29)
schedule_repository.save(schedule_30)
schedule_repository.save(schedule_31)
schedule_repository.save(schedule_32)