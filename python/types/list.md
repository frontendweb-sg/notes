# List in python

List are used to store multiple item in a single variable.

List items can be of any data type and contain different data types.

`Example:`

```py

# Create a number list
nums = [1,2,3,4,5,6]

# Contain different data types
list1 = ["abc", 34, True, 40, "male"]

# Create an empty list using [] or list() constructor
emptyList = []
# or
emptyList = list() # via list constructor

# create list via list() constructor
names = list(("Apple","Banana","JackFruits"))
```

<br />

`List Item:`

- List items are ordered, changable and allow duplicate values.
- List items are indexed, the first item has `index[0]`, the second item has `index[1]`.

`Fined the length:`

Use `len()` function to find the len.

```py
nums = [1,2,3,4,5]
print(len(nums)) # output: 5
```

`Access Items:`

```py
fruits = ["apple", "banana", "cherry"]
# first item has index 0
print(fruits[1])

# negative indexing start form the end, -1 refer to the last item, -2 refer to the second last item
print(fruits[-1]) # output: cherry


# Range of indexes, where to start and where to finish
print(fruits[0:2]) # output: [apple,banana], 2 index not included

# Range of negative indexes
print(fruits[-3:-1]) # output: [apple,banana], -1 not included

# Check if item is exist

if "apple" in fruits:
    print("Apple is in the list")

# Change item value
fruits[0] = "Orange"

# insert item at a specified index
fruits.insert(1,'papaya')

# add new item at the end
fruits.append('Mango')

# extend list
fruits.extend(('Grapes','Litchi'))

# Remove list item
fruits.remove('Litchi')

# pop
fruits.pop() # will remove last item
fruits.pop(1) # will remove first item

# del
del fruits[0] # will remove first item
del fruits # will delete the list completly

# Clear the list
fruits.clear()
```

<br />

`Loop:`

```py
# loop the list
for item in fruits:
    print(f'item: {item}')
```
