import unittest
from models.schedule import Schedule
import datetime

class TestSchedule(unittest.TestCase):
    def setUp(self):
        self.room = Schedule(datetime.date(2021, 03, 21))

    def test_room_has_name(self):
        self.assertEqual('Room 1', self.room.room_name)