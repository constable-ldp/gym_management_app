import unittest
import datetime
from models.member import Member 

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member('John', 'Smith', 'johnsmith@gmail.com', '07595964019', 
                             datetime.date(1997, 5, 17), True, False, datetime.date(2021, 3, 21),
                             datetime.date(2021, 4, 21))

    def test_member_has_first_name(self):
        self.assertEqual('John', self.member.first_name)

    def test_member_has_last_name(self):
        self.assertEqual('Smith', self.member.last_name)

    def test_member_has_email(self):
        self.assertEqual('johnsmith@gmail.com', self.member.email)
    
    def test_member_has_phone(self):
        self.assertEqual('07595964019', self.member.phone)

    def test_member_has_date_of_birth(self):
        self.assertEqual('1997-05-17', str(self.member.date_of_birth))

    def test_member_has_membership(self):
        self.assertEqual(True, self.member.membership)

    def test_member_has_premium(self):
        self.assertEqual(False, self.member.premium)

    def test_member_has_member_since(self):
        self.assertEqual('2021-03-21', str(self.member.member_since))

    def test_member_has_member_until(self):
        self.assertEqual('2021-04-21', str(self.member.member_until))