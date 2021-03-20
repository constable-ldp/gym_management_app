import unittest
from models.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('Room 1', 24, 'Large Room')

    def test_room_has_name(self):
        self.assertEqual('Room 1', self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(24, self.room.capacity)

    def test_room_has_description(self):
        self.assertEqual('Large Room', self.room.description)
