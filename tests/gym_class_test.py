import unittest
from models.gym_class import GymClass

class TestGymClass(unittest.TestCase):

    def setUp(self):
        self.gym_class = GymClass('Hot Yoga', 
                                  'Vigorous form of yoga performed in a very warm studio', 
                                  30, 60, 4, 16)

    def test_class_has_name(self):
        self.assertEqual('Hot Yoga', self.gym_class.name)

    def test_class_has_description(self):
        self.assertEqual('Vigorous form of yoga performed in a very warm studio', 
                         self.gym_class.description)

    def test_class_has_min_time(self):
        self.assertEqual(30, self.gym_class.min_time)
    
    def test_class_has_max_time(self):
        self.assertEqual(60, self.gym_class.max_time)

    def test_class_has_min_capacity(self):
        self.assertEqual(4, self.gym_class.min_capacity)

    def test_class_has_max_capacity(self):
        self.assertEqual(16, self.gym_class.max_capacity)