__author__ = 'dvir'
import tkFileDialog
import sqlite3

conn = sqlite3.connect(tkFileDialog.askopenfilename())
c = conn.cursor()


def has_inf(col, tbl, info):
    if len(c.execute(
         "SELECT '" + col + "' FROM '" + tbl + "' WHERE '"+col+"' = '" + id + "' AND '" + col + "' = '" + info + "'")) > 0:
        print col + " already exists"
        return True
    else:
        print col + " is OK"
        return False

