# Class in python

**`Class metadata:`**

In Python,

Class metadata refers to information about a class that is stored within the class itself.
This metadata can include `attributes`, `methods` and other class-specific data that can be used to inspect
or interact with the class programmatically.

`Class Attributes:`

Clas attributes are `variables` that belong to the class rather than `instance` of the class.
They are defined within the class body and can be accessed using the class `name` or `instances`.

`Example:`

```py
class User:
    # class attribute
    username:str = "Pradeep Kumar"

# access class attribute
print(User.username)
```

`Class Methods:`

Class methods are methods that operate on the class itself rather than on instances of the class.
They are defined using the `@classmethod` decorator.

`Example:`

```py
class User:
    # class attribute
    username:str = "Pradeep Kumar"

    # class mthod
    @classmethod
    def display(cls):
        print(cls.usernmae)

# access class method
print(User.display())
```

`Static Methods:`

Static methods are similar to regular functions but belong to the class's namespace.
They do not have access to `class` or `instance` data.

They are defined using the `@staticmethod` decorator.

`Example:`

```py
class User:
    # class attribute
    username:str = "Pradeep Kumar"

    # class mthod
    @classmethod
    def display(cls):
        print(cls.usernmae)

    # class static mthod
    @staticmethod
    def display_static():
        return "Hello, class static method"

# access class method
print(User.display_static())
```

`Using __dict__ Attribute:`

The \_\_dict\_\_ attribute of a class contains a dictionary of the class's attributes and methods.

`Example:`

```py
class User:
    # class attribute
    username:str = "Pradeep Kumar"

    # class mthod
    @classmethod
    def display(cls):
        print(cls.usernmae)

    # class static mthod
    @staticmethod
    def display_static():
        return "Hello, class static method"

# access class method
print(User.__dict__)
```

`Inspecting Classes:`

The `inspect` module provides functions for getting information about live objects, including classes.

`Example:`

```py
import inspect

class MyClass:
    class_attr = 'value'
    def method(self):
        pass

# Inspecting class members
print(inspect.getmembers(MyClass))
```
