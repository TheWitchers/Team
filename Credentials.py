__author__ = 'dvir'

import time
import hashlib


from dvir_methods_suggs import *





# 100-client
def register(ssl_sock, use, pas, email, fname, lname, nick, ver, ans):
    l ="100|"+ nick + "|" + email + "|" + fname + "|" + lname + "|" + use + "|" + pas + "|" + ver + "|" + ans
    ssl_sock.write(l)


# 101-server
def register_check(ssl_sock,reg_info ):
    l = reg_info.split("|")
    if not has_inf("username", l[5]) and not has_inf("email", l[1]) and not has_inf("nickname", l[0]):

        ssl_sock.write("Register Success")
        return "101",(True,l,)
    else:
        ssl_sock.write("Register Failed")
        return "101",(False,)

# 102-client
def login(ssl_sock, use, pas):
    ssl_sock.write("102|" + use + "|" + pas)


# 103-server
def login_check(ssl_sock, info):
    b = info.split("|")
    use = b[0]
    pas = b[1]
    if has_inf("username", use):
        conn = sqlite3.connect("DataBase\TeamDB.db")
        c = conn.cursor()
        l = []
        for row in c.execute("SELECT * FROM Users WHERE  username = '" + use + "' AND password = '" + pas + "'"):
            l.append(row[4])
            l.append(row[5])
        if len(l) > 0:
            # TODO: instead of l[] (list), will be session cookie
            # THE COOCKIE
            decookie = hashlib.sha1(use + "|" + pas + "|" + time.strftime("%d/%m/%Y %H:%M:%S")).hexdigest()
            ssl_sock.write(decookie)
            return "103",(decookie,use)

    else:
        ssl_sock.write("902")
        return "103",("902",)


# 104-client
def forgot_pas(ssl_sock, use):
    ssl_sock.write("104|" + use)


# 105-server
def ver_question(ssl_sock, use):
    q = c.execute("SELECT VerificationQuestion FROM Users WHERE username = '" + use + "'")
    ssl_sock.write("105|" + use)
