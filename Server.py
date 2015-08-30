__author__ = 'yagel'

from Credentials import *
import re
import socket, ssl, sys
import threading
from utils import strip_message


def init():
    bindsocket = socket.socket()
    bindsocket.bind(('127.0.0.1', 4567))
    bindsocket.listen(10)
    while True:
        newsocket, fromaddr = bindsocket.accept()
        ssl_sock = ssl.wrap_socket(newsocket,
                                   server_side=True,
                                   certfile="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.crt",
                                   keyfile="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.key")
        yield ssl_sock
#data = ssl_sock.read()

# divides the data to message code and actual data


def mc_handling(mc):
    chain_func={"100":"101","102":"103"}
    return chain_func[mc]

def example(connection, data):
    pass

funcs = {"100": register, "101": register_check, "102": login, "103": login_check, "104": forgot_pas, "105": ver_question}

def server(connection):
    while True:
        try:
            data = connection.recv(4096)
            mc, data = strip_message(data)
            funcs[mc_handling(mc)](connection, data)
        except:
            pass
            print "Unexpected error:", sys.exc_info()[0]
            connection.close()
            # close_thread()
            break

def main():
    threads = []
    while True:
        clienter = init()
        threads.append(threading.Thread(target=server, args=(clienter.next(),)))
        threads[-1].start()
main()
