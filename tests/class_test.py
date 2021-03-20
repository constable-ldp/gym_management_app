import unittest
from models.class import Class

class TestClass(unittest.TestCase):

    def SetUp(self):
        self.class = Class('Hot Yoga', 
                               'Vigorous form of yoga performed in a very warm studio', 
                                30, 60, 4, 16)

    def test_class_has_name(self):
        self.assertEqual('Hot Yoga', self.class.name)

    def test_class_has_description(self):
        self.assertEqual('Vigorous form of yoga performed in a very warm studio', 
                         self.class.description)

    def test_class_has_min_time(self):
        self.assertEqual(30, self.class.min_time)
    
    def test_class_has_max_time(self):
        self.assertEqual(60, self.class.max_time)

    def test_class_has_min_capacity(self):
        self.assertEqual(4, self.class.min_capacity)

    def test_class_has_max_capacity(self):
        self.assertEqual(16, self.class.max_capacity)