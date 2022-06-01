from multiprocessing import Process,Queue
from queue import Empty
import os
import time
import random
from core import actions
q = Queue()


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

# def f(q):
#     b=0
#     while True:
#         # time.sleep(0.1)
#         # b+=1
#         q.put([random.randrange(1,100,1),b])


def ff(qI):
    q.put(qI)
    print("queue size####################################################",q.qsize())

    


def start_processes():
    # print("start processes")
    # p = Process(target=f, args=(q,))
    # p.daemon=True
    # p.start()
    pass
    
def randomAct():
    t=random.randint(0, 7)
    if t==0:
        p = Process(target=ff, args=(actions.walk(),))
        p.daemon=True
        p.start()
    if t==1:
        # print("StTTTTands")
        p = Process(target=ff, args=(actions.stand(),))
        p.daemon=True
        p.start()
    if t==2:
        p = Process(target=ff, args=(actions.boring(),))
        p.daemon=True
        p.start()
    if t==3:
        p = Process(target=ff, args=(actions.lie(),))
        p.daemon=True
        p.start()
    if t==4:
        p = Process(target=ff, args=(actions.pull(),))
        p.daemon=True
        p.start()
    if t==5:
        p = Process(target=ff, args=(actions.run(),))
        p.daemon=True
        p.start()
    if t==6:
        p = Process(target=ff, args=(actions.sing(),))
        p.daemon=True
        p.start()
    print("randomAct")




    # currentMovie = random.choice(self.allActions)
def nothingToDo(father):
    randomAct()
    # q.put(actions.walk(father))
    print("nothingToDo")
    # currentMovie = random.choice(self.allActions)

    # time.sleep(6)
    # print(q.get())    # prints "[42, None, 'hello']"
    
#     try:
#         print(q.get(block=False))    # prints "[42, None, 'hello']"
#     except Empty:
#          print("clean")
#     # p.join()
# a()