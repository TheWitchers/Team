__author__ = 'yagel'


class UserDetails:
    def __init__(self,nickname,
                 email,
                 first_name,
                 last_name,
                 id ,
                 password,
                 verQuestion,
                 ans):
        self.id = id
        self.password=password
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.verQuestion = verQuestion
        self.ans = ans
        # self.payment_info = payment_info
        # self.age = age
        # self.phone = phone
        # self.birthdate = birthdate

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

        # another option is returning a list or a tuple-like string
        # return str([self.nickname, self.first_name, self.last_name, self.age, self.phone, self.email, self.birthdate])
         return str((self.id,
                    self.password,
                    self.nickname ,
                    self.first_name,
                    self.last_name,
                    self.email,
                    self.verQuestion ,
                    self.ans ))