from models.gym_class import GymClass
import repositories.gym_class_repository as class_repository
from models.member import Member
import repositories.member_repository as member_repository
import datetime

class_1 = GymClass('Hot Yoga', 
                   'Vigorous form of yoga performed in a very warm studio', 
                    30, 60, 4, 16)
class_repository.save(class_1)

class_2 = GymClass('CrossFit', 'Bodyweight workout', 45, 90, 6, 24)
class_repository.save(class_2)

member_1 = Member('John', 'Smith', 'johnsmith@gmail.com', '07595964019', 
                 datetime.date(1997, 5, 17), True, False, datetime.date(2021, 3, 21),
                 datetime.date(2021, 4, 21))
member_repository.save(member_1)