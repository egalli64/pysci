"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Python without NumPy
"""

from array import array

# a native list (of anything)
list = [x + 1 for x in range(6)]
list[-1] = "something different"
print(f"An object of type {type(list)}: {list}")

# try to generate a native array from the list above
try:
    native_array = array("i", list)
except TypeError as ex:
    print("Python native array are homogeneous:", ex)

# data cleaning, remove the non-int from the list
list = [x if isinstance(x, int) else -1 for x in list]

# a native int array (from an int-only iterable)
native_array = array("i", list)
print(f"An object of type {type(native_array)}: {native_array}")
