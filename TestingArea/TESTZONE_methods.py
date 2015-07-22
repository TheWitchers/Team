__author__ = 'dvir'
import tkFileDialog
import sqlite3

conn = sqlite3.connect(tkFileDialog.askopenfilename())
c = conn.cursor()

# using example db

def ex_show_purch(price):
    l = []
    for row in c.execute("SELECT symbol FROM stocks WHERE price > " + str(price) + ""):
        print row
        l.append(row)
    print l
    return l


ex_show_purch(raw_input("Enter Price: "))

# for project db

def show_purch(name):
    l = []
    for row in c.execute("SELECT * FROM Purchaseses WHERE nickname = '" + name + "'"):
        print row
        l.append(row)
    print l
    return l


def correct_user(id, pas):
    if len(c.execute("SELECT * FROM Users WHERE username = '" + id + "' AND password = '" + pas + "'")) > 0:
        print "user exists"
    else:
        print "user does not exist"
