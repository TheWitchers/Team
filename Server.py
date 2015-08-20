__author__ = 'yagel'

from Credentials import *
# from utils import strip_message

# divides the data to message code and actual data
def strip_message(data):
    l=[]
    for info in range(1, len(data)):
        l.append(info)
    return data[0],l

def mc_handling(mc):
    chain_func={"100":"101","102":"103"}
    return chain_func[mc]


def example(connection, data):
    pass


funcs = {"100": register(), "101": register_check(), "102": login(), "103": login_check(),"104": forgot_pas(),"105": ver_question()}


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
