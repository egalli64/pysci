"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Indexing on 2D array
"""

import numpy as np

throws = np.random.randint(1, 7, size=(2, 3))
print("All throws:\n", throws)

# Single index returns a full row
print("First row:", throws[0])
print("Last row:", throws[-1])

# Use a N-tuple to specify the actual position in a N-Dim array
print(f"First ({throws[0, 0]}) and last ({throws[0, -1]}) die in the first row")
print(f"First ({throws[-1, 0]}) and last ({throws[-1, -1]}) die in the last row")

# same for write access
throws[0, 0] = 10
throws[0, 1] += 10
# can't change data type - the value is silently truncated!
throws[0, 2] = 7.5
print("First row after editing:", throws[0])
