__author__ = 'dvir'
from PaymentInfos import PaymentInfo
class Purchases:
    def __init__(self, app_id, deal_num, product_name, buyer, deal_date, payment_info):
        self.app_id = app_id
        self.deal_num = deal_num
        self.product_name = product_name
        self.buyer = buyer
        self.deal_date = deal_date
        self.payment_info = payment_info

    def get_app_id(self):
        return self.app_id

    def set_app_id(self, id):
        self.app_id = id

    def get_deal_num(self):
        return self.deal_num

    def set_deal_num(self, num):
        self.deal_num = num

    def get_product_name(self):
        return self.product_name

    def set_product_name(self, name):
        self.product_name = name

    def get_buyer(self):
        return self.buyer

    def set_buyer(self, buyer):
        self.buyer=buyer

    def get_deal_date(self):
        return self.deal_date

    def set_deal_date(self,date):
        self.deal_date=date

    def get_payment_info(self):
        return self.payment_info

    def set_payment_info(self, info):
        self.payment_info= info