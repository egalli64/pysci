"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Logical operators
"""

import numpy as np

xs = np.random.randint(1, 11, size=6)
print("xs is", xs)

evens = xs % 2 == 0
print("Check even values:", evens)
lows = xs <= 5
print("Check low values: ", lows)

try:
    # logical operators won't work
    np.sum(evens and lows)
except ValueError as ex:
    print("Use bitwise operators -", ex)

print("Check for even and low values /1:", evens & lows)
print("Check for even and low values /2:", np.bitwise_and(evens, lows))

print("Check for even or low values /1:", evens | lows)
print("Check for even or low values /2:", np.bitwise_or(evens, lows))

print("Check for odd values:", ~evens)
print("Check for odd values:", np.bitwise_not(evens))
