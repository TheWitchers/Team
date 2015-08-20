__author__ = 'dvir'

import socket
import ssl
import pprint

def menu():
    print """
    1. Register
    2. Login
    """
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = ssl.wrap_socket(s,
                           ca_certs="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.crt",
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('127.0.0.1', 4567))

print repr(ssl_sock.getpeername())
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())

menu()
ssl_sock.write(raw_input("Enter username: "))
# ssl_sock.write("dviryamin1")
while True:
    a = ssl_sock.read()
    print a
    menu()

    if a != "":
        break
