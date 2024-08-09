# AsyncIO

It is a library to write `concurrent` code using the `async/await` syntax;

asyncio is used as a `foundation` for multiple Python `asynchronous frameworks` that provide

- high-performance network
- web-servers,
- database connection libraries,
- distributed task queues,
- etc

`asyncio` is often a perfect fit for `IO-bound` and `high-level` structured network code.

**`Basics:`**

`asyncio` allow you to write asyncrounous code that can handle multiple tasks concurrently.

At its core, it introduce the concepts of

- `Event loop:`

  Manages and dispatches events and tasks. It runs in the background and derives the asyncronous operations.

- `Coroutine:`

  A special function defined with `async def` that can use `await` to pause and resume its execution.

- `Tasks:`

  A wrapper for a coroutine that schedules it to run on the event loop.

`Example:`

```py
import asyncio

# it is asynchronous coroutine
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


# it is another coroutine
async def main():
    await say_hello()

# Running the event loop
if __name__ == "__main__":
    asyncio.run(main()) # runs the main coroutine and handles the event loop for you.
```

`await` is used to pause the coroutine until the awaited operation completes.

```py
async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulates a delay
    print("Data fetched!")
    return "Some data"

async def process_data():
    data = await fetch_data()
    print(f"Processing {data}")

if __name__ == "__main__":
    asyncio.run(process_data())
```

<br />

**`Running multiple task concurrently:`** use `async.gather`

```py
async def task1():
    await asyncio.sleep(2)
    return "Task 1 completed"

async def task2():
    await asyncio.sleep(1)
    return "Task 2 completed"

async def main():
    results = await asyncio.gather(task1(), task2()) # it will return results in list
    print(results)

if __name__ == "__main__":
    asyncio.run(main())

```

`asyncio.gather` runs `task1` and `task2` concurrently and waits for both to complete. The results are collected in a list.

<br />

**`Handling Exception in Asynchronous code:`**

```py
async def risky_task():
    await asyncio.sleep(1)
    raise ValueError("An error occurred")

async def main():
    try:
        await risky_task()
    except ValueError as e:
        print(f"Handled exception: {e}")

if __name__ == "__main__":
    asyncio.run(main())

```

<br />

**`Creating and managing tasks:`**

Tasks are a higher-level API for scheduling coroutines. You can create tasks explicitly using `asyncio.create_task()`.

```py
import asyncio

async def say_hello(name):
    print(f"Hello {name}")
    await asyncio.sleep(1)
    print(f"Goodbye {name}")

async def main():
    tasks = [
        asyncio.create_task(say_hello("Alice")),
        asyncio.create_task(say_hello("Bob")),
        asyncio.create_task(say_hello("Charlie")),
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
```

`Explanation:`

- `asyncio.create_task():` schedules the coroutines to run concurrently.
- `asyncio.gather(*tasks):` ensures all tasks are completed before proceeding.

<br />

**`Cancellation and Timeouts:`**

Tasks can be cancelled, and you can set timeouts using `asyncio.wait_for`.

```py
import asyncio

async def long_running_task():
    try:
        await asyncio.sleep(10)
        return "Finished"
    except asyncio.CancelledError:
        return "Cancelled"

async def main():
    task = asyncio.create_task(long_running_task())
    try:
        result = await asyncio.wait_for(task, timeout=5)
        print(result)
    except asyncio.TimeoutError:
        task.cancel()
        print("Task timed out and was cancelled")

if __name__ == "__main__":
    asyncio.run(main())
```

`Explanation:`

- `asyncio.wait_for()` applies a timeout to the task.
- If the task exceeds the timeout, it's cancelled.

<br />

**`Synchronization Primitives:`**

asyncio provides synchronization primitives like `Event`, `Lock`, `Semaphore`, and `Condition`.

`Using an asyncio.Lock:`

```py
import asyncio

lock = asyncio.Lock()

async def critical_section(name):
    async with lock:
        print(f"{name} has entered the critical section")
        await asyncio.sleep(2)
        print(f"{name} is leaving the critical section")

async def main():
    await asyncio.gather(
        critical_section("Task1"),
        critical_section("Task2")
    )

if __name__ == "__main__":
    asyncio.run(main())
```

`Explanation:`

- `asyncio.Lock` ensures that only one coroutine can access the critical section at a time.

**`Asynchronous Iterators:`**

Asynchronous iterators are useful for streaming data or handling large datasets in chunks.

```py
import asyncio

class AsyncRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __aiter__(self):
        self.current = self.start
        return self

    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration
        await asyncio.sleep(1)  # Simulating async I/O operation
        self.current += 1
        return self.current - 1

async def main():
    async for number in AsyncRange(1, 5):
        print(number)

if __name__ == "__main__":
    asyncio.run(main())
```

`Explanation:`

- AsyncRange implements \_\_aiter\_\_ and \_\_anext\_\_ for asynchronous iteration.
