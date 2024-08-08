# What are threads

In computing, `threading` allows a program to run multiple tasks (or `threads`) at the same time.

Each thread is like a small job that the computer can do simultaneously with other threads.

**`Creating thread in python:`**

Use `threading` module for python3 or `_thread` for using old module

```py
from threading import Thread,active_count
import time


def display():
    print("Hello World: start")
    time.sleep(1)
    print("Hello world: end")


# create seprate thread
# args: provide arguments to the target function
t1 = Thread(target=display, args=())

# execute thread (start)
t1.start()

print("Execute in main thread")
print("Check running thread: {}".format(active_count()))

# Wait for both threads to finish
thread1.join()
thread2.join()
```

`Note:`

- `Thread:` This creates a new thread. You pass a function (target) that the thread will execute.

- `start():` This begins the execution of the thread. It runs the function in a separate thread.
- `join():` This waits for the thread to finish its job before moving on. It's like making sure your cake is done baking before you open the oven door.

<br />

**`Global interpreter lock:`**

Python has something called the Global Interpreter Lock `(GIL)`. It's a mechanism that prevents multiple native threads from executing python BYTECODES at once.

This means that while threads can be useful, Python threads are not always perfect for CPU-bound tasks (tasks that require a lot of processing power).

However, they work well for `I/O-bound` tasks (tasks that wait for external resources, like downloading files).

`Pros:`

- Esures thread safety
- Improves single thread performance
- Prevents simultaneous multi-threading.
  - Bad for CPU limited tasks
- I/O limited threads are hardly affected.

`Example:`

```py
import threading

lock = threading.Lock()

def thread_function():
    with lock:
        # Critical section of code
        # Only one thread can enter this section at a time
        print("Thread is working")
```

<br />

**`Synchronization with locks:`**

Sometimes, `threads` need to share data. Just like when multiple people use the same oven, you need to be careful not to mix up the ingredients. In threading, you use synchronization tools like Locks to prevent threads from interfering with each other.

`Example:` Thread-safe counter

```py
import threading

# Shared resource
counter = 0
lock = threading.Lock()

# Thread function
def increment():
    global counter
    for _ in range(1000):
        with lock:  # Only one thread can execute this block at a time
            counter += 1

# Start threads
threads = [threading.Thread(target=increment) for _ in range(10)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")

```

`Lock():` This is a synchronization primitive. When a thread is in the critical section of code (where it needs to access shared resources), it locks the section so that no other thread can access it at the same time.

<br />

**`Using Conditions for Coordination:`**

Conditions are used when threads need to wait for certain conditions to be met before proceeding.

`Example:` Producer-Consumer with Condition

```py
import threading
import time

buffer = []
buffer_size = 5
condition = threading.Condition()
stop_signal = False  # Signal to stop the threads

# Producer thread
def producer():
    global buffer, stop_signal
    while not stop_signal:
        with condition:
            if len(buffer) >= buffer_size:
                condition.wait()  # Wait if buffer is full
            item = len(buffer) + 1
            buffer.append(item)
            print(f"Produced {item}")
            condition.notify()  # Notify consumer
        time.sleep(1)

    print("Producer exiting")

# Consumer thread
def consumer():
    global buffer, stop_signal
    while not stop_signal or buffer:
        with condition:
            if not buffer:
                if stop_signal:
                    break
                condition.wait()  # Wait if buffer is empty
            item = buffer.pop(0)
            print(f"Consumed {item}")
            condition.notify()  # Notify producer
        time.sleep(2)

    print("Consumer exiting")

# Start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Run for some time then signal stop
time.sleep(10)  # Let the producer and consumer run for a while
with condition:
    stop_signal = True
    condition.notify_all()  # Notify both threads to check the stop_signal

# Wait for threads to finish
producer_thread.join()
consumer_thread.join()

print("Program finished")

```

<br />

**`Communication between threads:`**

Threads often need to communicate or share results.

- Using `queues` for communication:

  `Queues` are a thread-safe way to pass data between threads. Python's `queue.Queue` is particularly useful.

`Example:` Producer-Consumer problem

```py
import threading
import queue
import time

# Create a queue
q = queue.Queue()

# Producer thread
def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)  # Add item to the queue
        time.sleep(1)  # Simulate time-consuming task

# Consumer thread
def consumer():
    while True:
        item = q.get()  # Retrieve item from the queue
        if item is None:  # End signal
            break
        print(f"Consuming {item}")
        time.sleep(2)  # Simulate time-consuming task

# Start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # Signal consumer to exit
consumer_thread.join()

```

`Producer:` Put item into the queue. <br />
`Consumer:` Takes items out of the queue and processes them. <br/>
`None:` The `None` signal is used to let the consumer know when to stop.

<br />

**`Thread local storage:`**

Thread-local storage (TLS) is a concept where each thread has its own separate instance of a variable or resource, allowing threads to maintain their own state independently of others. This is particularly useful in multithreaded programs where you need to keep data isolated between threads to avoid conflicts and ensure thread safety.

`Understand thread local storage:`

- Purpose of thread-local storage:

  Thread-local storage is used to store data that is specific to a particular thread. This ensures that the data is not shared between threads, preventing issues that arise from concurrent access to shared data.

- Using `threading.local()` in Python:

  This class creates an object where each thread has its own separate instance of the data stored in that object.

`Example:` Thread-Local Storage

```py
import threading

# Create a thread-local storage object
thread_local = threading.local()

def thread_function(name):
    # Set thread-local data
    thread_local.name = name
    print(f"Thread {name}: {thread_local.name}")

def main():
    # Create multiple threads, each with its own name
    thread1 = threading.Thread(target=thread_function, args=("A",))
    thread2 = threading.Thread(target=thread_function, args=("B",))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
```

`Example:2` A Counter

```py
import threading

# Thread-local storage
thread_local = threading.local()

def thread_function():
    thread_local.value = 0
    for _ in range(10):
        thread_local.value += 1
        print(f"Thread local value: {thread_local.value}")

thread1 = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

`Advantage of thread-local storage:`

- Isolation:

  Each thread has its own instance of data, eliminating conflicts from concurrent access.

- Simplified Code:

  Avoids the need for explicit synchronization mechanisms (e.g., locks) when dealing with thread-specific data.

- Efficiency:

  Reduces overhead associated with managing shared resources and locking mechanisms.

`Limitation and considerations:`

- Memory uses:

  Since each thread has its own instance of data, using a large number of threads can lead to increased memory usage.

- Global Data:

  Thread-local storage does not automatically manage global state or data that needs to be shared across threads.

- Garbage Collection:

  Be mindful of thread-local data lifecycle management to avoid potential memory leaks.

`Thread-local with context manager:`

```py
import threading

class ThreadLocalData:
    def __init__(self):
        self.local = threading.local()

    def set_data(self, key, value):
        setattr(self.local, key, value)

    def get_data(self, key):
        return getattr(self.local, key, None)

def thread_function(data_store, key, value):
    data_store.set_data(key, value)
    print(f"Thread {threading.current_thread().name} set {key} to {data_store.get_data(key)}")

def main():
    data_store = ThreadLocalData()

    # Create multiple threads
    thread1 = threading.Thread(target=thread_function, args=(data_store, 'data', 'value1'), name='Thread-1')
    thread2 = threading.Thread(target=thread_function, args=(data_store, 'data', 'value2'), name='Thread-2')

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
```

<br />

**`Thread vs Process in python:`**

|               | Threads                        | Process                    |
| ------------- | ------------------------------ | -------------------------- |
| Set-up cost   | Low                            | Hight                      |
| Handled by    | CPython interpreter            | OS                         |
| Memory Access | Shared                         | Seprate memory space       |
| Execution     | Concurrent <br /> non-parallel | Concurrent <br /> Parallel |

<br />

**`Avoiding Data Sharing Pitfalls:`**

-` Avoid Global State:` Minimize the use of global variables. Instead, pass data via thread-safe structures like queues or use thread-local storage (threading.local()).

- `Immutable Data:` Use immutable data structures (e.g., tuples) where possible to avoid unintended modifications.

- `Thread-Local Storage:` For data that should be unique to each thread, use threading.local().
