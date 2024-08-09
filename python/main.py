from threading import *
import time


sema = Semaphore(3)


def display():
    with sema:
        print("thread name: {}".format(current_thread()))
        print("Semaphore start: {}".format(sema._value))
        time.sleep(3)
        print("Semaphore done: {}".format(sema._value))


threads = [Thread(target=display) for _ in range(20)]

for t in threads:
    t.start()


for t in threads:
    t.join()


print("Finisih thread exextions: {}".format(current_thread()))
