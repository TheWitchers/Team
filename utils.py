__author__ = 'yagel'

def strip_message(data):
    data = data.split("|")
    code = data[0]
    data = data[1:]
    return code, data
