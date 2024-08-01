"""
Q1: Find the maximum and minimum value in tuple?
A1: Use math module to import "max" and "min" function.
"""

import math

nums = [4, 2, 7, 9, 10, 55, 22]
# min
print(min(nums))  # 2
# max
print(max(nums))  # 55


"""
Q2: Maximum and Minimum K elements in Tuple?
A2: Useing sorted() + loop
"""


def kElment(list, k):
    # k element
    # list is tuple
    result = []
    for index, value in enumerate(sorted(list)):
        if index < k or index >= len(list) - k:
            result.append(value)
    return tuple(result)


result = kElment(nums, k=2)
print(result)

"""
Q3: Python program to create a list of tuples from given list having number and its cube in each tuple
A3: Use list comphrension
"""

list_num = [2, 3, 4, 5]
list_cube = [(x, x**3) for x in list_num]
print(list_cube)

"""
Q4: Adding tuple to list and vice versa...
A4: using += operator [list+tuple]
"""

test_list = [5, 6, 7]
test_tup = (9, 10)

test_list += test_tup
# or
test_list.extend(list(test_tup))

print("The container after addition : " + str(test_list))
