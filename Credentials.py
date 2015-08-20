__author__ = 'dvir'

import socket
import ssl
import pprint
import time
from dvir_methods_suggs import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = ssl.wrap_socket(s,
                           ca_certs="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.crt",
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('127.0.0.1', 4567))

repr(ssl_sock.getpeername())
ssl_sock.cipher()
pprint.pformat(ssl_sock.getpeercert())

# 100-client
def register(use, pas, email, fname, lname, nick, ver, ans):
    l = [use, pas, email, fname, lname, nick, ver, ans]
    ssl_sock.write(l)


# 101-server
def register_check():
    l=[]
    if not has_inf("username", l[0]) and not has_inf("email", l[2]) and not has_inf("nickname", l[5]):
        c.execute(
            "INSERT INTO Users VALUES ('" + l[5] + "','" + l[2] + "','" + l[3] + "','" + l[4] + "','" + l[0] + "','" +
            l[1] + "', False,'" + l[6] + "','" + l[7] + "')")
        ssl_sock.write(True)
    else:
        ssl_sock.write(False)

# 102-client
def login(use, pas):
    l = [102, use, pas]
    ssl_sock.write(l)
    # ssl_sock.write("102|"+use+"|"+pas)

# 103-server
def login_check(use, pas):
    if has_inf("username", use):
        conn = sqlite3.connect("C:\Users\dvir\PycharmProjects\Team\DataBase\TeamDB.db")
        c = conn.cursor()
        l = []
        for row in c.execute("SELECT * FROM Users WHERE  username = '" + use + "' AND password = '" + pas + "'"):
            l.append(row[4])
            l.append(row[5])
        if len(l) > 0:
            # TODO: understand better what is session cookie and how to use it
            # TODO: instead of l[] (list), will be session cookie
            ssl_sock.write("Username: " + use + "\r\n" + "password: " + pas +"\r\n " + time.strftime("%d/%m/%Y %H:%M:%S"))
    else:
        ssl_sock.write("such user does not exist")

# 104-client
def forgot_pas(use):
    ssl_sock.write([use, 104])

# 105-server
def ver_question(use):
    q = c.execute("SELECT VerificationQuestion FROM Users WHERE username = '" + use +"'")
    ssl_sock.write(q)