import unittest
from models.instructor import InstructorDetails, InstructorSchedule
import datetime

class TestInstructorDetails(unittest.TestCase):

    def setUp(self):
        self.instructor = InstructorDetails('Mary', 'Jones', datetime.date(1992, 3, 12))

    def test_instructor_has_first_name(self):
        self.assertEqual('Mary', self.instructor.first_name)

    def test_instructor_has_last_name(self):
        self.assertEqual('Jones', self.instructor.last_name)

    def test_instructor_has_date_of_birth(self):
        self.assertEqual('1992-03-12', str(self.instructor.date_of_birth))

class TestInstructorSchedule(unittest.TestCase):

    def setUp(self):
        self.instructor_dets = InstructorDetails('Mary', 'Jones', datetime.date(1992, 3, 12))
        self.instructor = InstructorSchedule(datetime.date(2021, 3, 22), True, True, True, 
                                             True, True, False, False, datetime.time(9, 0), 
                                             datetime.time(17, 0), self.instructor_dets)
    
    def test_instructor_has_week_start_date(self):
        self.assertEqual('2021-03-22', str(self.instructor.week_start_date))

    def test_instructor_has_instructor(self):
        self.assertEqual('Mary', self.instructor.instructor.first_name)

    def test_instructor_has_day(self):
        self.assertEqual(True, self.instructor.monday)
        self.assertEqual(True, self.instructor.tuesday)
        self.assertEqual(True, self.instructor.wednesday)
        self.assertEqual(True, self.instructor.thursday)
        self.assertEqual(True, self.instructor.friday)
        self.assertEqual(False, self.instructor.saturday)
        self.assertEqual(False, self.instructor.sunday)

    def test_instructor_has_start_time(self):
        self.assertEqual('09:00:00', str(self.instructor.start_time))

    def test_instructor_has_end_time(self):
        self.assertEqual('17:00:00', str(self.instructor.end_time))

    
