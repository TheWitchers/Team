__author__ = 'dvir'
#from PaymentInfos import PaymentInfo
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