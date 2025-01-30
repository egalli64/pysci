"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Broadcasting a scalar
"""

import numpy as np

# adding two same sized arrays
a_array = np.arange(1, 4)
b_array = np.arange(6, 3, -1)
print(f"No broadcast: {a_array} + {b_array} = {a_array + b_array}\n")

# scalar and 1D, 2D, 3D array
print("Broadcasting a scalar onto a one-dimensional array")
alpha = 3
print(f"{a_array} + {alpha} = {a_array + alpha}")
print(f"{a_array} - {alpha} = {a_array - alpha}")
print(f"{alpha} - {a_array} = {alpha - a_array}\n")

print("Broadcasting a scalar onto a 2D array")
eye = np.eye(3, dtype=int)
print(f"{eye} + {alpha} is ...\n{eye + alpha}\n")

print("Broadcasting a scalar onto a 3D array")
m3d = np.ones((3, 2, 2), dtype=np.int_)
print(f"{m3d} + {alpha} is ...\n{m3d + alpha}\n")
