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
