a = 10
b = a  # 'b' now refers to the same object as 'a'

# Checking memory addresses
print(id(a))  # Output: Memory address of object 'a'
print(id(b))  # Output: Memory address of object 'b', should be the same as 'a'

# Modifying 'a' does not change its memory address
a: int = 20
print(id(a))  # Output: Memory address of new object 'a'

# 'b' still refers to the old object (integer '10')
print(b)  # Output: 10
print(id(b))  # Output: Memory address of object 'b', same as original 'a'
