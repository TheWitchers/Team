__author__ = 'dvir'
import tkFileDialog
import sqlite3

conn = sqlite3.connect("C:\Users\dvir\PycharmProjects\Team\DataBase\TeamDB.db")
c = conn.cursor()


def has_inf(col, tbl, info):
    if len(c.execute(
         "SELECT '" + col + "' FROM '" + tbl + "' WHERE '"+col+"' = '" + id + "' AND '" + col + "' = '" + info + "'")) > 0:
        print col + " already exists"
        return True
    else:
        print col + " is OK"
        return False


def extract_inf(col, tbl, info):
    if has_inf(col, tbl, info):
        return c.execute("SELECT * FROM '"+tbl+"' WHERE '"+col+"' = '" + str(info) + "'")
    else:
        print "info does not exist"

