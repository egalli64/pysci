"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Slicing a 1D array, use of step
"""

import numpy as np

a = np.arange(10)
print("An array:", a)

# start, end, step
print("Start in 2, end in 8 (excluded), step by 3:", a[2:8:3])

# start, ..., step
print("All elements with odd index, start 1, step 2:", a[1::2])

# ..., end, step
print("First elements with even index, end 6 (excluded), step 2:", a[:6:2])

# ..., ..., step
print("All elements with even index:", a[::2])

# reversing an array
print("Reversed:", a[::-1])

xs = a[::-2]
print("Reversed skipping any other element:", xs)

# in any case, a slice is always a view
xs[0] = 42
print("Both original and slice changes:", a, xs)
