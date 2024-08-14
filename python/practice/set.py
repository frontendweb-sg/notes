"""
Q1: Get the size of the set, means the amount of memory sets occupied.
A1: We will use the getsizeof() function that belongs to 'sys' module
"""
import sys
set1 = {1, 2, 3, 4, 5}

# unpack the set
x, *y = set1
print(f"x-{x}")

print(set1.pop())

print("{} bytes".format(sys.getsizeof(set1)))


# Max and minimum in set
print(max(set1))
print(min(set1))

# remove item from set
set1.remove(4)
print(set1)

# check two list have at least one element common
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

print(set(list1).intersection(list2))


sq = {x for x in range(1, 10) if x % 2 == 0}
print(sq)

try:
    set1.remove(6)
except KeyError:
    print("Key does not exist")
