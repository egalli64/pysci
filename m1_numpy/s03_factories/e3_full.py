"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

ndarray factories full() and empty()
"""

import numpy as np

# full
print("full of -1:", np.full(3, -1))
print("\nfull of -1, 2 rows and 3 columns:\n", np.full((2, 3), -1))

# empty
print("\nempty (uninitialized):", np.empty(3))
print("\nnempty, 2 rows and 4 columns:\n", np.empty((2, 4), dtype=int))
