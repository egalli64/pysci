"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

The "out" parameter
"""
import numpy as np

array = np.arange(1, 7)
target = np.empty(6)
print("Input:", array)

# sending output to the specified sink
np.multiply(array, 10, out=target)
print("Target:", target)

xs = array[:3]
print("Input (view):", xs)
# the sink could be a view, too
sink = target[::2]
print("Before changing the sink (view):", sink)
np.power(2, xs, out=sink)
print("After changing sink and target:", sink, target)
