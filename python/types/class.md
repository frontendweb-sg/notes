# Classes in python

In `Python`,

A `class` is a blueprint for creating `objects` (instances) that encapsulates `data` (attributes) and `functionality` (methods).

Classes provide a way to bundle data and functionality together, making it easier to manage and reuse code.

`Creating class:`

```py
class Car:
    # Class attribute, shared by all instances
    category = "Vehicle"

    # Constructor method (initializer)
    def __init__(self, make, model, year):
        # Instance attributes, unique to each instance
        self.make = make
        self.model = model
        self.year = year

    # modify str method
    def __str__(self):
        return f"Car(yar:{self.year}, make:{self.make},model:{self.model})"

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Tesla", "Model S", 2023)

# Accessing attributes and calling methods
print(car1.display_info())  # Output: 2022 Toyota Camry
print(car2.display_info())  # Output: 2023 Tesla Model S
print(car1.category)        # Output: Vehicle
print(car2.category)        # Output: Vehicle
```

`In this example:`

- `Car` is a class that defines a blueprint for creating car objects.

- `category` is a class attribute shared by all instances of the class.

- `__init__` is a special method (constructor) that initializes new instances of the class (car1 and car2) with specific attributes (make, model, year).

- `__str__` is an special method that provides a formatted string representation of the car's class.

<br />

**`Class and Instance Variables:`**

In Python, variables defined within a class are either class variables or instance variables:

- `Class variables` are shared among all instances of the class. They are defined outside of any method.

- `Instance variables` are unique to each instance of the class. They are typically defined within the `__init__` method using self.

```py
class Car:
    # Class variable
    category = "Vehicle"

    def __init__(self, make, model, year):
        # Instance variables
        self.make = make
        self.model = model
        self.year = year
```

<br />

**`Class method:`**

- You can also add class methods to your custom Python classes.
- A class method is a method that takes the class object as its first argument instead of taking `self`.
- In this case, the argument should be called `cls`.

You can create class methods using the `@classmethod` decorator.

Providing your classes with `multiple constructors` is one of the most common use cases of class methods in `Python`.

```py
# point.py
class ThreeDPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        yield from (self.x, self.y, self.z)

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y}, {self.z})"

# instance of ThreeDots
ThreeDPoint.from_sequence((4, 8, 16))
```

<br />

**`Static method:`**

- Your Python classes can also have static methods.
- These methods don’t take the instance or the class as an argument.
- So, they’re regular functions defined within a class.
- You could’ve also defined them outside the class as stand-alone function.

```py
# point.py

class ThreeDPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        yield from (self.x, self.y, self.z)

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 3D Point!")

    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y}, {self.z})"


ThreeDPoint.show_intro_message("Pythonista")
# Hey Pythonista! This is your 3D Point!
```
