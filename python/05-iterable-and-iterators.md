# Iterables and Iterators

**`Iterables:`**

An `iterable` is any python object that can return an iterator.

in other words, an iterable is an object that implement `__iter()__` method or has a `__getitem()__` method that can be used to fetch items by `index`.

`Common examples of iterables include:`

- List
- Tuple
- Set
- Dictionary
- String
- Generator

`To check object is iterable:`

Use `iter()` function

```py
# Lists are iterable
nums = [1,2,3]
is_iterable = iter(nums) # Returns an iterator
print(next(is_iterable))

# Strings are iterable
my_string = "hello"
iterator = iter(my_string)  # Returns an iterator
print(next(iterator))  # Output: 'h'
```

<br />

**`Iterators:`**

An `iterators` is an python object that return a stream of data. it returns one element at a time when you call the `__next()__` function.

Iterators must implement two methods:

- `__iter()__:` This method return the iterator object itself.
- `__next()__:` This method returns the item from the iterator. When there are no more items to return , it raises the `StopIteration` exeeption.

```py
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Creating an iterator
my_iter = MyIterator([1, 2, 3])
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
# print(next(my_iter))  # Raises StopIteration
```

<br />

**`Iterable vs Iterators:`**

- `Iterable:`

  - Can be passed to `iter()` to get an iterator.
  - Has an `__iter()__` method.
  - Examples: list, tuples, strings

- `Iterator:`
  - Represents a stream of data and keeps track off its own state.
  - Must implement `__iter__()` and `__next__()`.
  - Examples: iterator object that retured by `iter()`

<br />

`itertools:`

Python's `itertools` module provides various functions to work with iterators.
Functions include `chain(),` `cycle()`, `count()`, `islice()`, `zip_longest()`, etc

```py
import itertools

# Count with a step
counter = itertools.count(start=0, step=2)
for _ in range(5):
    print(next(counter))
# Output: 0, 2, 4, 6, 8

# Chain iterables
chained = itertools.chain([1, 2], [3, 4])
print(list(chained))  # Output: [1, 2, 3, 4]

```

<br />

**`Performance and use-cases:`**

1. `Efficiency:`

   - Iterators are generally more memory-efficient than lists because they generate items one at a time.
   - Useful for handling large datasets or infinite sequences (e.g., streaming data).

2. `Lazy Evaluation:`

   - Iterators and generators support lazy evaluation, meaning values are computed on-the-fly.
   - This is particularly useful for data pipelines where you only process items as needed.

3. `State Management:`

   - Iterators maintain their own state, which can be advantageous for certain algorithms and operations.

4. `Compatibility:`
   - Iterators can be used with Python’s built-in functions and libraries that accept iterables, such as map(), filter(), and reduce()
