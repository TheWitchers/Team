__author__ = 'dvir'
import sqlite3
# a = tkFileDialog.askopenfilename()
conn = sqlite3.connect("C:/Users/dvir/PycharmProjects/Team/DataBase/TeamDB.db")
# print a
c = conn.cursor()

a = "y"
while a == "y":
    c.execute("INSERT INTO Users VALUES ('"
              + raw_input("Enter nickname: ") + "', '"
              + raw_input("Enter email: ") + "', '"
              + raw_input("Enter first name: ") + "', '"
              + raw_input("Enter last name: ") + "', '"
              + raw_input("Enter username: ") + "', '"
              + raw_input("Enter password: ") + "', "
                                                "'false','"
              + raw_input("Enter verefication question: ") + "', '"
              + raw_input("Enter answer: ") + "')")

    # c.execute("INSERT INTO 'Users' VALUES ('dvirking', 'dviryamin@gmail.com', 'dvir', 'yamin', 'dviryamin', 'schrhnhi','false','some', 'some')")
    a = raw_input("continue? ('y' to proceed)")
for row in c.execute("SELECT * FROM Users"):
    print row

a = raw_input("save changes? ('y' to save)")
if a == "y":
    conn.commit()
