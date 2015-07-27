__author__ = 'dvir'
import tkFileDialog
import sqlite3

conn = sqlite3.connect(tkFileDialog.askopenfilename())
c = conn.cursor()


def has_inf(cols, tbl, field_name=False, field_value=False):
    query = "SELECT "
    for col in cols:
        query += col + ","
    query = query[:-2]  # Remove last , .
    query += " FROM " + tbl + " "
    if field_name and field_value:
        query += "WHERE '" + field_name + "' = " + field_value
    answer = c.execute("SELECT * FROM Users WHERE username = '" + id)
    answer = answer.fetchall()
    if len(answer) > 0:
        print col + " already exists"
        return True
    else:
        print col + " is OK"
        return False
