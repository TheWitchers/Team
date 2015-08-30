__author__ = 'yagel'

def strip_message(data):
    data = data.split("|")
    code = data[0]
    data[0].remove()
    data='|'.join(data)
    #data = data[1:]
    return code, data
