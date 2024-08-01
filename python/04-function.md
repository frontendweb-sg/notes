# Functions

# Decorators

A `decorator` is a design pattern that allow you to modifiy the functionality of a function by wrapping it in another function.

`Syntax:`

**Defining a Decorator:**

```py
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
```

**Using a Decorator:**

```py
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

`Example:`

```py
def dec_fun(original_fun):
    def wrapper():
        print("Wrapper execution this before {}".format(original_fun.__name__))
        return original_fun()
    return wrapper;


@dec_fun
def hello():
    """Document for the hello world"""
    print("Hello World")
```

**Decorator with arguments:**

```py
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```
