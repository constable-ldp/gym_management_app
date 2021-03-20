import unittest
import datetime
from models.member import Member 

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member('John', 'Smith', 'johnsmith@gmail.com', '07595964019', datetime.date(1997, 5, 17), True, False)

    def test_member_has_first_name(self):
        self.assertEqual('John', self.member.first_name)

    def test_member_has_last_name(self):
        self.assertEqual('Smith', self.member.last_name)

    def test_member_has_email(self):
        self.assertEqual('johnsmith@gmail.com', self.member.email)
    
    def test_member_has_phone(self):
        self.assertEqual('07595964019', self.member.phone)

    def test_member_has_date_of_birth(self):
        self.assertEqual('John', self.member.date_of_birth)

    def test_member_has_membership(self):
        self.assertEqual(True, self.member.membership)

    def test_member_has_premium(self):
        self.assertEqual(False, self.member.premium)