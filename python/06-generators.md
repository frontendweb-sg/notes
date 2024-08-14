# Generators

A `generator` is a special type of `iterator` that is defined using a function with the `yield` keyword.

When you call a generator function it return an generator object.

`Basic structor of generator:`

```py
def gen():
    yield 1
    yield 2
    yield 3


item = gen()
print(next(item))

# or

def MyRange(start: int, end: int):
    count = start
    while count < end:
        yield count
        count += 1

items = MyRange(0,5)
print(next(items))

# or

for i in MyRange(0,5):
    print(i)


# Generator expressions
squares = (x * x for x in range(5))
for square in squares:
    print(square)
```

**`How generators work:`**

- `State Preservation:`

  Genrators autometically preserve their state between `yield` statements. When a `yeild` is executed, the function's state is saved, including local variable and the execution point.

- `Lazy Evalution:`

  Generators produce items one at a time only when required. this means they are memory efficent and can represent large sequences without storing them all in memory.

- `Iteration:`

  Each call to `next()` on a generator resumes exection from where it left off.

<br />

**`Advanced Generator Features:`**

- `Generator methods:`

  Generator can also use the `send()` method to send values back into the generator, and `throw()` to throw and exception into the generator.

  ```py
    def gen():
        while True:
            value = (yield)
            print(f"Received: {value}")


    g = gen()
    next(g)
    g.send("Hello World")

    # throw error

    def gen1():
        try:
            yield
        except ValueError:
            print("Value error")

    g1 = gen1()
    next(g1)
    gen.throw(ValueError)
  ```

<br />

**`Practical use case:`**

- `Data Processing Pipelines:`
  Generators are useful for building pipelines that process large amount of data.
  such as:

  - Reading from files.
  - Applying transformations.
  - filtering data.

- `Infinite Sequence:`
- `Concurrency:`
