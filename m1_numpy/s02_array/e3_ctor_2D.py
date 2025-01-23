"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

2-D ndarray
"""

import numpy as np
from ndarray_checker import check

# two rows, three columns
check(np.array([range(i, i + 3) for i in range(2)]))

# three rows, two columns
check(np.array([range(i, i + 2) for i in range(3)]))
