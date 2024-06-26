# Set in python

In `Python`,

a set is an unordered collection of unique elements.

It's defined using curly braces `{}` and can contain elements of different data types, such as integers, floats, strings, and tuples, but not mutable types like lists or dictionaries.

- `Unordered:` Sets do not maintain the order of elements as they are added.

- `Unique Elements:` A set cannot contain duplicate elements. If you try to add a duplicate element, it will be ignored.

- `Mutable:` Sets are mutable, meaning you can add or remove elements after creation.

- `Supports Mathematical Set Operations:` Sets support operations like union, intersection, difference, and symmetric difference.

**`Creating set:`**

You can create a set in Python using curly braces `{}` or the `set()` function.

```py
# using curly braces {}
my_set = {1, 2, 3, 4, 5}

# using set()
my_set = set([1, 2, 3, 4, 5])

# adming elements
# use add() for adding single element
my_set.add(6)

# use update() for adding multiple element
my_set.update([7, 8])

# removing elements
# Use the remove() method to remove a specific element. If the element is not present, a KeyError is raised.
my_set.remove(3)

# Use discard() method to remove an element if it is present, without raising any error.
my_set.discard(10)  # No error even if 10 is not in the set
```

**`Set operation:`**

```py
# Union (|): Combines elements from two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # {1, 2, 3, 4, 5}

# Intersection (&): Returns elements common to both sets.
intersection_set = set1 & set2  # {3}

# Difference (-): Returns elements in the first set but not in the second.
difference_set = set1 - set2  # {1, 2}

# Symmetric Difference (^): Returns elements in either set, but not both.
symmetric_difference_set = set1 ^ set2  # {1, 2, 4, 5}

# iterating over set
for element in my_set:
    print(element)

# Frozenset
# Python also provides a built-in frozenset type,
frozen_set = frozenset([1, 2, 3])

```
