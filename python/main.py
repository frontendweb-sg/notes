
import concurrent.futures

from threading import Thread, current_thread
import time


def display(n, main):
    print('n-', current_thread().name)
    time.sleep(1)
    for x in range(n):
        print(f'x-{x}-{main}')


start = time.perf_counter()
t1 = Thread(target=display, kwargs={'n': 100, 'main': 'child-thread'})
t1.start()
t1.join()
end = time.perf_counter()

display(10, 'main-')
print(f'Finished in {round(end-start, 2)} seconds')
