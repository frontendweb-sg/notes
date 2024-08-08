# Multiprocessing Module

`multiprocessing` is a `package` that supports `spawning` processes using an `API` similar to the `threading` module.

The `multiprocessing` package offers both `local` and `remote` `concurrency` effectively side-stepping the `Global Interpreter Lock` by using `subprocesses` instead of `threads`.

The `multiprocessing` module in Python is a powerful tool for parallelizing tasks and managing multiple processes.

. It allows you to bypass Python's Global Interpreter Lock`(GIL)`and use multiple CPUs effectively.

**`Basic Concepts:`**

- `Process:`
  An instance of a pythong interpreter. Each process runs independently.
- `Queue:`
  A thread-safe FIFO (First-In,First Out) queue for exchanging data between processes.
- `Pipe:`
  A way to create tow-way communication channel between processes.
- `Pool:`
  A pool of worker processes for parallel execution of tasks.

`Process: `

processes are spawned by creating a `Process` object and then calling its `start()` method.
`Process` follows the api of `threading.Thread`.

```py
from multiprocessing import Process

def worker(num):
    print(f'Worker: {num}')

if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = Process(target=worker, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
```

To show the individual process IDs involved

```py
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
```

<br />

**`Contexts and start methods:`**

Depending on the plateform, multiprocessing supports three ways to start `process`.

- `spwan:`

  The parent process starts a fresh Python interpreter process.

  The child process will only inherit those resources necessary to run the process object’s `run()` method.

  In particular, unnecessary file descriptors and handles from the parent process will not be inherited. Starting a process using this method is rather slow compared to using fork or forkserver.

  The default on `Windows` and `macOS`.

- `fork:`

  The parent process uses `os.fork()` to fork the Python interpreter.

  The child process, when it begins, is effectively identical to the parent process.

  All resources of the parent are inherited by the child process. Note that safely forking a multithreaded process is problematic.

  Currently the default on `POSIX` except `macOS`.

- `forkserver:`

  When the program starts and selects the forkserver start method, a server process is spawned. From then on, whenever a new process is needed, the parent process connects to the server and requests that it fork a new process. The fork server process is single threaded unless system libraries or preloaded imports spawn threads as a side-effect so it is generally safe for it to use` os.fork()`. No unnecessary resources are inherited.

To select a start method you use the `set_start_method`() in the if **name** == '**main**' clause of the main module.

`For example:`

```py
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

`Note:` set_start_method() should not be used more than once in the program.

`Alternatively`, you can use `get_context`() to obtain a context object.

```py
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

<br />

**`Exchanging objects between processes:`**

multiprocessing supports two types of `communication` channel between `processes`:

- `Queues:`
  The `Queue` class is a near clone of `queue.Queue`.
  `For example:`

  ```py
  from multiprocessing import Process, Queue

  def f(q):
      q.put([42, None, 'hello'])

  if __name__ == '__main__':
      q = Queue()
      p = Process(target=f, args=(q,))
      p.start()
      print(q.get())    # prints "[42, None, 'hello']"
      p.join()
  ```

  `Queues` are thread and process safe. Any object put into a multiprocessing queue will be serialized.

<br />

- `Pipes:`

  The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way).

  `For Example:`

  ```py
  from multiprocessing import Process, Pipe

  def f(conn):
      conn.send([42, None, 'hello'])
      conn.close()

  if __name__ == '__main__':
      parent_conn, child_conn = Pipe()
      p = Process(target=f, args=(child_conn,))
      p.start()
      print(parent_conn.recv())   # prints "[42, None, 'hello']"
      p.join()
  ```

  The two connection objects returned by `Pipe()` represent the two ends of the pipe. Each connection object has `send()` and `recv()` methods (among others).

  `Note:`

  that data in a pipe may become corrupted if two processes (or threads) try to read from or write to the same end of the pipe at the same time. Of course there is no risk of corruption from processes using different ends of the pipe at the same time.

  The send() method serializes the the object and recv() re-creates the object.

<br />

**`Parallel Processing with a Pool:`**

`Problem:`

Suppose you have a CPU-bound task that you want to parallelize. For instance, you want to compute the square of numbers in parallel.

`Solution:`

Use `Pool` to distribute the task among multiple worker processes.

```py
from multiprocessing import Pool
import time

def compute_square(n):
    print(f'Processing number: {n}')
    time.sleep(1)  # Simulate a time-consuming computation
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    with Pool(processes=4) as pool:
        results = pool.map(compute_square, numbers)

    print(results)  # Outputs: [1, 4, 9, 16, 25]

```

`Explanation:`

- `Pool(processes=4):` Creates a pool of 4 worker processes.
- `pool.map:` Distributes the compute_square function across the pool with the provided numbers. The results are collected and returned as a list.

**`Inter-Process Communication and Synchronization:`**

`Problem Statement`

You have multiple processes performing tasks, and you need to aggregate the results and synchronize the processes.

`Solution`

Use Queue for communication and Lock for synchronization.

```py
from multiprocessing import Process, Queue, Lock, current_process
import time

def worker(q, lock, num):
    with lock:
        print(f'{current_process().name} working on {num}')
        time.sleep(1)
        q.put(num * 2)  # Simulate some computation

if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    numbers = [1, 2, 3, 4, 5]

    processes = [Process(target=worker, args=(q, lock, num)) for num in numbers]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = []
    while not q.empty():
        results.append(q.get())

    print(results)  # Outputs: [2, 4, 6, 8, 10]

```

`Explanation`

- `Lock:` Ensures that only one process at a time can print to the console, avoiding jumbled output.

- `Queue:` Collects results from worker processes.

- `Empty Check:` Collects results from the queue after all processes have finished
