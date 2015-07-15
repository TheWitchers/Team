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
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
except:
    print("table already exists")
a=True

while a:
    c.execute("INSERT INTO stocks VALUES ('"+raw_input("enterDate")+"',"
                                   "'"+raw_input("BUY/SELL")+","
                                  "'"+raw_input("enterSymbol")+","
              "'666+,"
              "'6666)")
                                 #"'"+int(raw_input("enterQty"))+","
                                #"'"+int(raw_input("enterPrice"))+")")
    a=raw_input("contiue?")
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print row
print("end")