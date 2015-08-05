__author__ = 'dvir'
import tkFileDialog
import sqlite3

conn = sqlite3.connect("C:\Users\dvir\PycharmProjects\Team\DataBase\TeamDB.db")
c = conn.cursor()


def has_inf(col, info):
    l = []
    for row in c.execute(
         "SELECT " + col + " FROM Users WHERE  " + col + " = '" + info + "'"):
        l.append(row)
    if len(l) > 0:

        return True
    else:

        return False


def extract_inf(col, tbl, info):
    if has_inf(col, tbl, info):
        return c.execute("SELECT * FROM '"+tbl+"' WHERE '"+col+"' = '" + str(info) + "'")
    else:
        print "info does not exist"

