import unittest
from models.gym_class import GymClass

class TestGymClass(unittest.TestCase):

    def setUp(self):
        self.gym_class = GymClass('Hot Yoga', 'Yoga performed in a very warm studio', 60, 16)

    def test_class_has_name(self):
        self.assertEqual('Hot Yoga', self.gym_class.class_name)

    def test_class_has_description(self):
        self.assertEqual('Yoga performed in a very warm studio', self.gym_class.description)
    
    def test_class_has_max_time(self):
        self.assertEqual(60, self.gym_class.max_time)

    def test_class_has_capacity(self):
        self.assertEqual(16, self.gym_class.capacity)