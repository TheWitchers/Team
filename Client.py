__author__ = 'dvir'
import os
import pprint
import socket
import ssl

from utils import strip_message
from Credentials import *

global cookie
cookie = ""
def init():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global ssl_sock
    ssl_sock = ssl.wrap_socket(s,
                               ca_certs="TestingArea\server.crt",
                               cert_reqs=ssl.CERT_REQUIRED)
    ssl_sock.connect(('127.0.0.1', 4567))

    print repr(ssl_sock.getpeername())
    print ssl_sock.cipher()
    print pprint.pformat(ssl_sock.getpeercert())

def creat_cookie_file(cookie):
    try:
        file = open("cookie.txt",'w+')   # Trying to create a new file or open one
        file.write(cookie)
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')

def login_menu():
    if os.path.exists("cookie.txt"):
        file = open("cookie.txt",'r')
        global cookie
        cookie = file.read()
        file.close()

        auto_login(ssl_sock,cookie)
        print "Waiting for server...\n"
        data = ssl_sock.recv(2048)
        print data
        if data != "903":
            print "Recognized cookie"
            user_menu()
        else:
            print "Cookie is nor recognized"
            cookie = ""

    while cookie == "":
        print ("What do you want to do?\n"
               "    \n"
               "    1. Register\n"
               "    2. Login\n"
               "    3. Forgot password\n"
               "    4. Exit")

        b = input()
        if b == 1:
            register(ssl_sock,
                     raw_input("Enter username: "),
                     raw_input("Enter password: "),
                     raw_input("Enter email: "),
                     raw_input("Enter first name: "),
                     raw_input("Enter last name: "),
                     raw_input("Enter nickname: "),
                     raw_input("Enter verification question: "),
                     raw_input("Enter answer: "))

        elif b == 2:
            login(ssl_sock,
                  # raw_input("Enter username: "),
                  # raw_input("Enter password: "))
                  "dviryamin1",
                  "schrhnhi1")
            print "dviryamin1" \
                  "schrhnhi1"
            data = ssl_sock.recv(2048)

            if data != "902":
                global cookie
                cookie = data
                print cookie
                creat_cookie_file(data)
                user_menu()

            elif data == "902":
                print "can't login because use or pass not match"

        elif b == 3:
            forgot_pas(ssl_sock,raw_input("Enter username: "))
            quest = ssl_sock.read()
            print quest
            send_ver_ans(ssl_sock,(raw_input("Enter answer: ")))
            pas = ssl_sock.read()
            print pas
        elif b ==4:
            break
        else:
            print "Invalid input"

def user_menu():
    while cookie != "":
        print ("What do you want to do?\n"
               "    \n"
               "    1. Show your account info\n"
               "    2. Show store\n"
               "    3. Show games list\n"
               "    4. Logout")

        b = input()

        if b == 1:
            info_req(ssl_sock,cookie)
            print ssl_sock.read()
        elif b == 4:
            logout(ssl_sock, cookie)
            global cookie
            cookie = ""
        else:
            print "Invalid input"
def client_adjustment(data):
        return strip_message(data)

init()
login_menu()
blob = raw_input("Mr. poopy pants")
ssl_sock.close()
print cookie + "indic"
# s.close()
