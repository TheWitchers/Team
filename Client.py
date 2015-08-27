__author__ = 'dvir'

from Credentials import *
import pprint, socket, ssl
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# ssl_sock = ssl.wrap_socket(s,
#                            ca_certs="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.crt",
#                            cert_reqs=ssl.CERT_REQUIRED)
#
# ssl_sock.connect(('127.0.0.1', 4567))
#
# repr(ssl_sock.getpeername())
# ssl_sock.cipher()
# pprint.pformat(ssl_sock.getpeercert())
#

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
              raw_input("Enter username: "),
              raw_input("Enter password: "))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.crt",
                           cert_reqs=ssl.CERT_REQUIRED)
ssl_sock.connect(('127.0.0.1', 4567))

print repr(ssl_sock.getpeername())
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())

# ssl_sock.write(raw_input("Enter username: "))
menu()
"""
while True:
    a = ssl_sock.read()
    print a
    if a == "":
        break
"""
ssl_sock.close()
# s.close()
