class Member:
    def __init__(self, first_name, last_name, email, phone, date_of_birth, membership, premium = False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.membership = membership
        self.premium = premium