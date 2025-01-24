"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

The (nd)array constructor specifying dtype
"""

import numpy as np
from ndarray_checker import check

# a native list (of integer)
values = [x + 1 for x in range(6)]

# forcing the dtype
check(np.array(values, dtype=float))

check(np.array(values, dtype=complex))

values[-1] = "something different"

# each element in the passed iterable should be of a compatible type
try:
    xs = np.array(values, dtype=float)
except ValueError as ex:
    print("No ndarray created,", ex)
