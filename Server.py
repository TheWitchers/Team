__author__ = 'yagel'


from Credentials import *
# from utils import strip_message


def strip_message(data):
    pass


def example(connection, data):
    pass


funcs = {"100": register(),"101": register_check(), "102": login()}


def server(connection):
    while True:
        try:
            data = connection.recv(4096)
            mc, data = strip_message(data)
            funcs[mc](connection, data)
        except:
            connection.close()
            # close_thread()
            break
