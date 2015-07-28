__author__ = 'dvir'

import socket, ssl
from dvir_methods_suggs import extract_inf

bindsocket = socket.socket()
bindsocket.bind(('127.0.0.1', 4567))
bindsocket.listen(10)


def do_something(connstream, data):
    print data
    connstream.write(extract_inf("username", "Users", data))
    return False

def deal_with_client(connstream):
    data = connstream.read()
    while data:
        if not do_something(connstream, data):
            break
        data = connstream.read()

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = ssl.wrap_socket(newsocket,
                                 server_side=True,
                                 certfile="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.crt",
                                 keyfile="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.key")
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
