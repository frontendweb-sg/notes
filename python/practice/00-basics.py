import numpy as np

# show numpy version
print("========== SHOW VERSION ==========")
print(np.__version__)

# show build configuration
# Show libraries and system information on which NumPy was built and is being used
print("========== SHOW BUILD CONFIGURATION ==========")
print(np.show_config())

# show runtime info
print("========== SHOW RUNTIME ==========")
print(np.show_runtime())

# write a program to get help with the add function
# use 'np.info(func)' to get help of function
# print(np.info(np.add))

# numpy built-ins
# print(np.__builtins__)

# write a program to test whether none of the elements of a given array are zero
a = np.array([1, 2, 3, 4])
print(np.all(a), np.nan, np.inf)
