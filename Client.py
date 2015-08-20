__author__ = 'dvir'

from Credentials import *


def menu():
    print ("What do you want to do?\n"
           "    \n"
           "    1. Register\n"
           "    2. Login\n")

    b = raw_input()
    if b == 1:
        register(raw_input("Enter username: "),
                 raw_input("Enter password: "),
                 raw_input("Enter email: "),
                 raw_input("Enter first name: "),
                 raw_input("Enter last name: "),
                 raw_input("Enter nickname: "),
                 raw_input("Enter verification question: "),
                 raw_input("Enter answer: "))
    elif b == 2:
        login(raw_input("Enter username: "),
              raw_input("Enter password: "))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.crt",
                           cert_reqs=ssl.CERT_REQUIRED)
ssl_sock.connect(('127.0.0.1', 4567))

print repr(ssl_sock.getpeername())
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())

ssl_sock.write(raw_input("Enter username: "))

while True:
    a = ssl_sock.read()
    print a
    menu()

    if a != "":
        break

ssl_sock.close()
s.close()
