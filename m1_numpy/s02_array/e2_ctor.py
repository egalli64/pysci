"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

The (nd)array constructor
"""

import numpy as np
from ndarray_checker import check

# a native list (of anything)
values = [x + 1 for x in range(6)]

# NumPy int64 ndarray (inherently homogeneous)
my_array = np.array(values)
check(my_array)

# NumPy UTF-32 string max size 21 (U21), ndarray (forced to be homogeneous)
values[-1] = "something different"
my_array = np.array(values)
check(my_array)

# NumPy byte string, max size 21 (S21), ndarray (forced to be homogeneous)
values[-1] = b"something different"
my_array = np.array(values)
check(my_array)

# NumPy float64 ndarray (forced to be homogeneous)
values[-1] = 2 / 3
my_array = np.array(values)
check(my_array)
