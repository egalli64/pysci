"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

The "out" parameter
"""

import numpy as np

array = np.arange(1, 7)
print("Input:", array)

target = np.empty(6, np.int_)
print("Target:", array)

# sending output to the specified sink
np.multiply(array, 10, out=target)
print("Target after multiply input by 10:", target)

xs = array[:3]
print("A view on input:", xs)
# the sink could be a view, too
sink = target[::2]
print("A view on target:", sink)
np.power(2, xs, out=sink)
print("After sending output on the sink, the target changes too:", sink, target)
