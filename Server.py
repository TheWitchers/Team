__author__ = 'yagel'

from Credentials import *
import re
import socket, ssl

# from utils import strip_message

bindsocket = socket.socket()
bindsocket.bind(('127.0.0.1', 4567))
bindsocket.listen(10)

newsocket, fromaddr = bindsocket.accept()
ssl_sock = ssl.wrap_socket(newsocket,
                           server_side=True,
                           certfile="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.crt",
                           keyfile="C:\Users\dvir\PycharmProjects\Team\TestingArea\server.key")

data = ssl_sock.read()

# divides the data to message code and actual data
def strip_message(data):
    l=re.split('[|]',data)
    code = l[0]
    l.remove(l[0])
    return code,l

def mc_handling(mc):
    chain_func={"100":"101","102":"103"}
    return chain_func[mc]

def example(connection, data):
    pass

funcs = {"100": register, "101": register_check, "102": login, "103": login_check,"104": forgot_pas,"105": ver_question}

def server(connection):
    while True:
        try:
            data = connection.recv(4096)
            mc, data = strip_message(data)
            funcs[mc](connection, data)
            funcs[mc_handling(mc)](data)
        except:
            connection.close()
            # close_thread()
            break
server(ssl_sock)