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
        # return """
        #         nickname: %s
        #         first name: %s
        #         last name: %s
        #         age: %s
        #         phone: %s
        #         email: %s
        #         birthdate: %s
        #         payment info: (still in progress)
        #
        #         """ % (self.nickname, self.first_name, self.last_name, self.age, self.phone, self.email, self.birthdate)
        # another option is returning a list or a tuple
        # return str([self.nickname, self.first_name, self.last_name, self.age, self.phone, self.email, self.birthdate])
        # return str((self.nickname, self.first_name, self.last_name, self.age, self.phone, self.email, self.birthdate))
        pass
        # TODO: Implement this method.
