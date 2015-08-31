__author__ = 'yagel'

import socket
import ssl
import sys
import threading

from Credentials import *
from utils import strip_message

funcs = {"100": register, "101": register_check, "102": login, "103": login_check, "104": forgot_pas,
         "105": ver_question}
cookie = {}


def init():
    bindsocket = socket.socket()
    bindsocket.bind(('127.0.0.1', 4567))
    bindsocket.listen(10)
    while True:
        newsocket, fromaddr = bindsocket.accept()
        ssl_sock = ssl.wrap_socket(newsocket,
                                   server_side=True,
                                   certfile="TestingArea\server.crt",
                                   keyfile="TestingArea\server.key")
        yield ssl_sock


def mc_handling(mc):
    #
    try:
        chain_func = {"100": "101", "102": "103"}
        if mc in chain_func:
            return chain_func[mc]


    except:
        print "problam"


def example(connection, data):
    pass


def server(connection):
    while True:
        try:
            data = connection.read()
            print data
            if data != '':
                mc, data = strip_message(data)
                funcs[mc_handling(mc)](connection, data)
            elif data=='':

                raise
        except:
            if data == '':
                print "the client connection has shut down"
            connection.close()
            #threading.Thread.close_thread()

            break


def main():
    threads = []
    while True:
        clienter = init()
        threads.append(threading.Thread(target=server,
                                        args=(clienter.next(),)))

        threads[-1].start()


main()
