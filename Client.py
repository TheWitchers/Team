__author__ = 'dvir'

import pprint
import socket
import ssl

from utils import strip_message
from Credentials import *

cookie=""

def menu():
    print ("What do you want to do?\n"
           "    \n"
           "    1. Register\n"
           "    2. Login\n")

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
        print "ID: dviryamin\n" \
              "Password: schrhnhi1"
        data = ssl_sock.recv(2048)
        if data != "902":
            cookie = data
            print cookie
        elif data == "902":
            print "can't login because use or pass not match"

    elif b == 3:
        forgot_pas(ssl_sock,raw_input("Enter username: "))

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

def client_adjustment(data):
        return strip_message(data)

init()
menu()
blob = raw_input("Mr. poopy pants")
ssl_sock.close()
# s.close()
