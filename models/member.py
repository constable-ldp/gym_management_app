class Member:

    def __init__(self, first_name, last_name, email, phone, date_of_birth, membership=False,
                 premium=False, member_since=None, member_until=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.membership = membership
        self.premium = premium
        self.member_since = member_since
        self.member_until = member_until
        self.id = id
