__author__ = 'dvir'
import sqlite3

conn = sqlite3.connect("C:\Users\dvir\PycharmProjects\Team\DataBase\TeamDB.db")
c = conn.cursor()


def has_inf(col, tbl, info):
    l = []
    for row in c.execute(
                                            "SELECT * FROM Users WHERE '" + col + "' = '" + info + "'"):
        l.append(row)
    if len(l) > 0:
        print info + " already exists"
        return True
    else:
        print info + " is OK"
        return False


def extract_inf(col, tbl, info):
    if has_inf(col, tbl, info):
        return str(0 in c.execute("SELECT * FROM Users WHERE '" + col + "' = '" + str(info) + "'"))
    else:
        print "info does not exist"
        return ""
