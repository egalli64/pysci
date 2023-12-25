"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

The ndarray
"""
import numpy as np
from ndarray_checker import check

# a native list (of anything)
list = [x for x in range(10)]
list[-1] = "42"
print(f"An object of type {type(list)}: {list}")

if isinstance(list[-1], str):
    # Python native array
    from array import array

    # arrays are homogeneous, comment next line to get a TypeError
    list[-1] = 9

    # a native int array
    native_array = array("i", list)
    print(f"An object of type {type(native_array)}: {native_array}")


# NumPy unicode-32 string ndarray (forced to be homogeneous)
list[-1] = "hello"
check(np.array(list))

# NumPy integer ndarray (inherently homogeneous)
list[-1] = 9
check(np.array(list))

# NumPy float64 ndarray (forced to be homogeneous)
check(np.array(np.array([1, 2, 10 / 3])))

# 2-dimensional arrays
check(np.array([range(i, i + 3) for i in range(2)]))
check(np.array([[1, 2], [3, 4], [5, 6]]))

# forcing the dtype by argument
check(np.array([1, 2, 3], dtype=float))
check(np.array([[1, 2, 3], [4, 5, 6]], dtype=complex))
