# Tuple

In `Python`,

a tuple is a data structure that is similar to a list,
but with the key difference that `tuples` are `immutable`, meaning they cannot be changed after they are created. `Tuples` are defined by enclosing a comma-separated sequence of values within parentheses `()`.

**`When to Use Tuples:`**

- Use tuples when you want to store a fixed collection of items that should not change, such as days of the week, coordinates, or configuration settings.

- Tuples are also useful for returning multiple values from a function

**`Creating tuple:`**

```py
# Creating tuples
empty_tuple = ()
single_element_tuple = (5,)  # Note the trailing comma
multi_element_tuple = (1, 2, 3, 4, 5)
mixed_data_types_tuple = ('apple', 3.14, True)
nested_tuple = ((1, 2), ('a', 'b', 'c'))

print(f"empty: {empty_tuple} single_element: {single_element_tuple} mixed_data_types_tuple: {mixed_data_types_tuple}, duplicate_tuple: {duplicate_tuple} nested_tuple: {nested_tuple}")


# access tuple element by indexing
print(num[0],"zeroth element of num")


```

**`Tuple operation:`**

```py

# Tuple operation
# Since tuples are immutable, they do not have methods that can modify their contents like lists do.
# but you can convert tuple into list and perform addintion,removing and etc.
num_list = list(num)
print(num_list)

# slicing
my_tuple = ('a', 'b', 'c', 'd', 'e')
print(my_tuple[1:4])  # Output: ('b', 'c', 'd')

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

```

**`Method:`**

```py
my_tuple = ('a', 'p', 'p', 'l', 'e')
```

- `count:` Count occurrences of a value

  ```py
  print(my_tuple.count('p'))  # Output: 2

  ```

- `index:` Find index of a value

  ```py
  print(my_tuple.index('l'))  # Output: 3

  ```

**`Immutability and its Implications:`**

Tuples in Python are immutable, meaning once they are created, their contents cannot be changed.

- `Performance:` Tuples are more memory efficient than lists because they are fixed-size and immutable. This can lead to faster iteration and access times for large datasets.

- `Hashability:` Tuples are hashable, which means they can be used as keys in dictionaries and elements in sets (since their hash value never changes).

- `Safety in Data Integrity:` Immutable data structures are inherently safer in concurrent programming environments because they cannot be modified unexpectedly by different parts of a program.

**`Packing and Unpacking:`**

Python allows for convenient packing and unpacking of tuples. Packing is placing values into a tuple, while unpacking extracts values back into variables:

```py

# Packing
my_tuple = 1, 2, 3  # Parentheses are optional
print(my_tuple)  # Output: (1, 2, 3)

# Unpacking
x, y, z = my_tuple
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3

# using * asterik to collect remaining value in unpacking
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

# This feature is widely used in functions that return multiple values:

def get_coordinates():
    return 3, 4

x, y = get_coordinates()
print(f"x = {x}, y = {y}")  # Output: x = 3, y = 4



```

**`Tuple Comprehension (Generator Expressions):`**

Although tuples do not have a comprehension syntax like lists ([...]), you can create tuples using generator expressions wrapped in tuple():

```py
tuple_comp = tuple(x for x in range(5))
print(tuple_comp)  # Output: (0, 1, 2, 3, 4)

```
