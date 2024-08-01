# Python dictionary

In `Python`,

A dictionary is a built-in data structure that is used to store collections of items, where each item is a key-value pair.

A dictionary is a collection which is `ordered`\*, `changeable` and do `not allow duplicates`.

They are defined by enclosing a comma-separated list of key-value pairs within curly braces `{}`, where each pair is separated by a colon `:`.

**`Creating dictionary:`**

You can create a dictionary in Python using curly braces {} and specifying key-value pairs:

```py
# Creating dictionaries
empty_dict = {}
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements
print(person['name'])  # Output: 'John'
print(person['age'])   # Output: 30

# If a key does not exist, accessing it will raise a KeyError.
# To avoid this, you can use the .get() method which returns None if the key does not exist (or a specified default value):

print(person.get('city'))  # Output: 'New York'
print(person.get('job', 'Unknown'))  # Output: 'Unknown' (default value)

# Modifying and Adding elements
# Modifying elements
person['age'] = 32
print(person['age'])  # Output: 32

# Adding new elements
person['job'] = 'Engineer'
print(person)  # Output: {'name': 'John', 'age': 32, 'city': 'New York', 'job': 'Engineer'}

```

**`Methods:`**

- `.keys(), .values(), .items():` These methods return views of keys, values, and key-value pairs respectively.

- `.pop(key[, default]):` Removes and returns the value associated with the key. If the key is not found and a default value is provided, it returns that value.

- `.update(dict2):` Updates the dictionary with key-value pairs from another dictionary or iterable.

- `.clear():` Removes all items from the dictionary.

<br />

**`Dictionary Comprehensions:`**

```py
# Dictionary comprehension
numbers = {x: x * x for x in range(5)}
print(numbers)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

```
