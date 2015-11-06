__author__ = 'dvir'

import time
import hashlib

from dvir_methods_suggs import *



# 100-client
def register(ssl_sock, use, pas, email, fname, lname, nick, ver, ans):
    l = "100|" + nick + "|" + email + "|" + fname + "|" + lname + "|" + use + "|" + pas + "|" + ver + "|" + ans
    ssl_sock.write(l)


# 101-server
def register_check(ssl_sock, reg_info):
    l = reg_info.split("|")
    if not has_inf("username", l[5]) and not has_inf("email", l[1]) and not has_inf("nickname", l[0]):

        ssl_sock.write("Register Success")
        return "101", (True, l,)
    else:
        ssl_sock.write("Register Failed")
        return "101", (False,)


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
            # THE COOCKIE
            decookie = hashlib.sha1(use + "|" + pas + "|" + time.strftime("%d/%m/%Y %H:%M:%S")).hexdigest()
            ssl_sock.write(decookie)
            return "103", (decookie, use)

    else:
        ssl_sock.write("902")
        return "103", ("902",)


# 104-client
def forgot_pas(ssl_sock, use):
    ssl_sock.write("104|" + use)


# 105-server
def ver_question(ssl_sock, use):
    c.execute("SELECT VerificationQuestion FROM Users WHERE username = '" + use + "'")
    q = c.fetchone()[0]
    ssl_sock.write(q)
    lisen_ver_ans(ssl_sock, use)
    return "105", use


# 106-client
def send_ver_ans(ssl_sock, ans):
    ssl_sock.write(ans)


# 107-server
def lisen_ver_ans(ssl_sock, info):
    ans = ssl_sock.read()
    if c.execute("SELECT answer FROM Users WHERE username = '" + info + "'").fetchone()[0] == ans:
        ssl_sock.write(c.execute("SELECT password FROM Users WHERE username = '" + info + "'").fetchone()[0])


# 108-client
def info_req(ssl_sock, cookie):
    ssl_sock.write("108|" + cookie)


# 109-server
def send_client_info(ssl_sock, info):
    # conn = sqlite3.connect("DataBase\TeamDB.db")
    # c = conn.cursor()
    # info=c.execute("SELECT * FROM Users WHERE  username = '" + id+"'").fetchone()
    ssl_sock.write(str(info))
    return "109",info


# 110-client
def logout(ssl_sock, cookie):
    ssl_sock.write("110|" + cookie)


# 111-server
def dc_user(ssl_sock, ):
    # ssl_sock.write("111")
    pass


# 112-client
def auto_login(ssl_sock, cookie):
    ssl_sock.write("112|" + cookie)

# 113-client
def auto_login_check(ssl_sock, rslt):
    if rslt:
        ssl_sock.write("Pass")
        return "113","Pass"
    else:
        ssl_sock.write("903")
        return "113","903"