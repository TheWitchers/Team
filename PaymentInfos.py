__author__ = 'yagel'

from abc import ABCMeta, abstractmethod


class PaymentInfo(object):
    __metaclass__ = ABCMeta

    def __init__(self, method, name):
        self.method = method
        self.name = name

    @abstractmethod
    def charge(self, amount):
        pass

    @abstractmethod
    def check_validity(self):
        pass

    def get_method(self):
        return self.method

    def get_name(self):
        return self.name


class CreditCard(PaymentInfo):
    def __init__(self, name, card_number, exp_date, csc):
        super(CreditCard, self).__init__(1, name)
        self.card_number = card_number
        self.exp_date = exp_date
        self.csc = csc

    def charge(self, amount):
        pass
        # TODO: Implement this method.

    def check_validity(self):
        pass
        # TODO: Implement this method.


class BankAccount(PaymentInfo):
    def __init__(self, name, id_number, branch):
        super(BankAccount, self).__init__(2, name)
        self.id_number = id_number
        self.branch = branch

    def check_validity(self):
        pass
        # TODO: Implement this method.

    def charge(self, amount):
        pass
        # TODO: Implement this method.


class Coupon(PaymentInfo):
    def __init__(self, name, code):
        super(Coupon, self).__init__(3, name)
        self.code = code
        self.amount = self.check_amount()

    def charge(self, amount):
        pass
        # TODO: Implement this method.

    def check_validity(self):
        pass
        # TODO: Implement this method.

    def check_amount(self):
        pass
        # TODO: Implement this method.
