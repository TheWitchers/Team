__author__ = 'dvir'

from dvir_methods_suggs import *
import socket
import ssl
import pprint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = ssl.wrap_socket(s,
                           ca_certs="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.crt",
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('127.0.0.1', 4567))

repr(ssl_sock.getpeername())
ssl_sock.cipher()
pprint.pformat(ssl_sock.getpeercert())

# 100
def  register(use, pas, email, fname, lname, nick, ver, ans):
    l=[use, pas, email, fname, lname, nick, ver, ans]
    ssl_sock.write(l)
# 101
def register_check(l=[]):
    if not has_inf("username", l[0]) and not has_inf("email", l[2]) and not has_inf("nickname", l[5]):
        c.execute(
            "INSERT INTO Users VALUES ('" + l[5] + "','" + l[2] + "','" + l[3] + "','" + l[4] + "','" + l[0] + "','" + l[1] + "', False,'" + l[6] + "','" + l[7] + "')")
        ssl_sock.write(True)
    else:
        ssl_sock.write(False)
# 102
def login(use,pas):
    l = [use,pas]
    ssl_sock.write(l)


def login_check(use, pas):
    if has_inf("username", use):
        conn = sqlite3.connect("C:\Users\dvir\PycharmProjects\Team\DataBase\TeamDB.db")
        c = conn.cursor()
        l = []
        for row in c.execute("SELECT * FROM Users WHERE  username = '" + use + "' AND password = '" + pas + "'"):
            l.append(row[4])
            l.append(row[5])
        if len(l) > 0:
            # TODO: instead of l[], will be session cookie
            ssl_sock.write(l)
    else:
        return "such user does not exist"


