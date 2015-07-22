__author__ = 'dvir'
import sqlite3
import datetime
# not working on microsoft db formats. pypyodbc will work but no need for that now.
# conn = sqlite3.connect("D:\steamProjDB1_Backup.accdb")
# file=open('D:\example'+datetime.datetime+'.db','w+')
# file=open('D:\example.db','w+')
conn = sqlite3.connect("D:\example.db")
c=conn.cursor()
try:
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

except:
    print("table already exists")
a=True
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# while a == True:
#     c.execute("INSERT INTO stocks VALUES ('"+str(datetime.date.today()) + "',"
#                                       "'"+raw_input("BUY/SELL: ") + "',"
#                                       "'"+raw_input("enterSymbol: ") + "',"
#                                       ""+raw_input("enterQty: ") + ","
#                                       ""+raw_input("enterPrice: ") + ")")

    # a=raw_input("contiue?")
conn.commit()
def show_purch(price):
    l = []
    for row in c.execute("SELECT symbol FROM stocks WHERE price = " + str(price) + ""):
        print row
        l.append(row)
    print l
    return l
show_purch(raw_input("enterPrice: ") )
# for row in c.execute('SELECT * FROM stocks ORDER BY price'):
#         print row
# print("end")
conn.close()