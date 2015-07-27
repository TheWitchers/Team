__author__ = 'dvir'


class Game:
    def __init__(self, App_ID, Product_Name, Developer, price, Release_Date, tags, description, min_system, rate, times_rated,  Download_Link):
        self.app_id = App_ID
        self.product_name=Product_Name
        self.developer = Developer
        self.price = price
        self.release_date = Release_Date
        self.tags = tags
        self.description = description
        self.min_system = min_system
        self.rate = rate
        self.times_rated = times_rated
        self.available = True
        self.download_link = Download_Link

    def get_app_id(self):
        return self.app_id

    def set_app_id(self, appid):
        self.app_id = appid

    def get_product_name(self):
        return self.product_name

    def set_product_name(self, name):
        self.product_name=name

    def get_developer(self):
        return self.developer

    def set_developer(self, dev):
        self.developer =dev

    def get_release_date(self):
        return self.release_date

    def set_release_date(self, date):
        self.release_date = date

    def is_available(self):
        return self.available
