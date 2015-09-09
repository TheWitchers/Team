__author__ = 'dvir'
import sqlite3

conn = sqlite3.connect("DataBase\TeamDB.db",check_same_thread=False)
c = conn.cursor()


def has_inf(col, info):
    l = []
    for row in c.execute( "SELECT " + col + " FROM Users WHERE  " + col + " = '" + info + "'"):
        l.append(row)
    if len(l) > 0:

        return True
    else:

        return False

def extract_user_inf(use):

    try:
        for row in c.execute("SELECT * FROM Users WHERE  username = '" + use + "'"): # "AND password = '" + pas + "'"
            l=row
        return l
    except:
        print "error - in user extraction"


def extract_inf(col, tbl, info):
    if has_inf(col, tbl, info):
        return c.execute("SELECT * FROM '" + tbl + "' WHERE '" + col + "' = '" + str(info) + "'")
    else:
        print "info does not exist"
