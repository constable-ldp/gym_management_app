import unittest
from models.schedule import Schedule
import datetime

class TestSchedule(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule(datetime.date(2021, 3, 21), 45)

    def test_schedule_has_class_date(self):
        self.assertEqual('2021-03-21', str(self.schedule.class_date))

    def test_schedule_has_length_mins(self):
        self.assertEqual(45, self.schedule.length_mins)