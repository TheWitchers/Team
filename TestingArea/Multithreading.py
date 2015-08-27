__author__ = 'dvir'
import threading
import random


def Splitter(words):
    list = words.split()
    nlist = []
    while (list):
        nlist.append(list.pop(random.randrange(0, len(list))))

    print(' '.join(nlist))


if __name__ == '__main__':
    sen = 'Your god damn right.'
    numOfTreads = 5
    threadList = []

    print("STARTING...\n")
    for i in range(numOfTreads):
        t = threading.Thread(target=Splitter,
                             args=(sen,))
        t.start()
        threadList.append(t)

    print("\nTread Count: " + str(threading.activeCount()))
    print("EXITING...\n")
