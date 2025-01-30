"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Broadcasting 2D array
"""

import numpy as np

nines_2d = np.full((2, 2), 9)
print(f"{nines_2d} a 2D array")

ones_3d = np.ones((3, 2, 2), dtype=np.int_)
print(f"{ones_3d} a 3D array")

print("\nBroadcasting a 2D array onto a 3D array")
print(nines_2d + ones_3d)
