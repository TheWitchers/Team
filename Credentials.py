__author__ = 'dvir'
import sqlite3

from dvir_methods_suggs import *


class Credentials:
    def register(self, use, pas, email, fname, lname, nick, ver, ans):
        if not has_inf("username", use) and not has_inf("email", email) and not has_inf("nickname", nick):
            c.execute(
                "INSERT INTO Users VALUES ('" + nick + "','" + email + "','" + fname + "','" + lname + "','" + use + "','" + pas + "', False,'" + ver + "','" + ans + "')")

    def login(self, use, pas):
        if has_inf("username", use):
            conn = sqlite3.connect("C:\Users\dvir\PycharmProjects\Team\DataBase\TeamDB.db")
            c = conn.cursor()
            if 0 in c.execute(
                    "SELECT username,password FROM Users WHERE  username = '" + use + "' AND password = '" + pas + "'") != ():
                print 0 in c.execute(
                    "SELECT username,password FROM Users WHERE  username = '" + use + "' AND password = '" + pas + "'")
