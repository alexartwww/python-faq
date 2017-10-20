'''
GIL - Global Interpreter Lock
'''

from threading import Thread
from multiprocessing import Process

def writer(x):
    for i in range(1000000):
        pass

if __name__ == '__main__':
    # init threads
    t1 = Process(target=writer, args=(0, ))
    t2 = Process(target=writer, args=(1, ))

    # start threads
    t1.start()
    t2.start()

    # join threads to the main thread
    t1.join()
    t2.join()
