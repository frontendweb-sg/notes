from threading import *
from time import *

# Create a race condition
count = 0
lock = Lock()
condition = Condition()


def counter(n):
    print('n: {}'.format(n))
    global count
    for x in range(n):
        with condition:
            condition.wait()
            count += x
    print('-------------{}'.format(current_thread()))


threads = [Thread(target=counter, args=(10,)) for _ in range(10)]

for t in threads:
    t.start()

for thread in threads:
    thread.join()
print(f"counter : {count}")
