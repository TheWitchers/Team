__author__ = 'dvir'

import socket, ssl, sqlite3

conn = sqlite3.connect("C:/Users/dvir/PycharmProjects/Team/DataBase/TeamDB.db")
c = conn.cursor()


bindsocket = socket.socket()
bindsocket.bind(('127.0.0.1', 4567))
bindsocket.listen(10)

newsocket, fromaddr = bindsocket.accept()
connstream = ssl.wrap_socket(newsocket,
                             server_side=True,
                             certfile="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.crt",
                             keyfile="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.key")

data = connstream.read()

print data

l = []
for row in c.execute("SELECT * FROM Users WHERE username='" + data + "'"):
    l.append(row)
print l
connstream.write(str(l))