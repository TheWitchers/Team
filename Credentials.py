__author__ = 'dvir'
from dvir_methods_suggs import *
class Credentials:
    def register(self, use, pas, email, fname, lname, nick, ver, ans):
        if not has_inf("username", use) and not has_inf("email", email) and not has_inf("nickname", nick):
            c.execute(
                "INSERT INTO Users VALUES ('"+nick+"','"+email+"','"+fname+"','"+lname+"','"+use+"','"+pas+"', False,'"+ver+"','"+ans+"')")

