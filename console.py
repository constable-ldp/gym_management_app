from models.gym_class import GymClass
import repositories.gym_class_repository as class_repository

class_1 = GymClass('Hot Yoga', 
                   'Vigorous form of yoga performed in a very warm studio', 
                    30, 60, 4, 16)
class_repository.save(class_1)

class_2 = GymClass('CrossFit', 'Bodyweight workout', 45, 90, 6, 24)
class_repository.save(class_2)