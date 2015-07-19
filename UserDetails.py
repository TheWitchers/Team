__author__ = 'yagel'


class UserDetails:
    def __init__(self, nickname, first_name, last_name, age, phone, email, birthdate, payment_info):
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.email = email
        self.birthdate = birthdate
        self.payment_info = payment_info

    def __repr__(self):
        pass
        # TODO: Implement this method.
