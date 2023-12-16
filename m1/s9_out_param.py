"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

The "out" parameter
"""
import numpy as np

a = np.arange(1, 7)
target = np.empty(6)
print("Input:", a)

# sending output to the specified sink
np.multiply(a, 10, out=target)
print("Output:", target)

# the sink could be a view
a = a[3:]
print("Input:", a)
sink = target[::2]
print("Sink (before squaring):", sink)
np.power(2, a, out=sink)
print("Output:", target)
