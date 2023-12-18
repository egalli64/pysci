"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Factories for ndarray
"""
import numpy as np
from s2_ndarray_checker import check

print("*** zeros")
check(np.zeros(6))

print("*** ones")
check(np.ones((3, 2), dtype=int))

print("*** full")
check(np.full((2, 2, 2), 42, int))

print("*** array constructor + standard range")
check(np.array(range(2, 11, 2)))

print("*** arange")
check(np.arange(2, 11, 2))

print("*** arange on floats")
check(np.arange(1.0, 1.51, 0.1))

print("*** linear space, 5 integers in [2, 10]")
check(np.linspace(2, 10, 5, dtype=int))

print("*** linear space, 6 values in [1.0, 1.5]")
check(np.linspace(1.0, 1.5, 6))

print("*** logarithmic space, 5 values in [10**0, 10**2]")
check(np.logspace(0, 2, 5))

print("*** Three random values (uniform distribution)")
check(np.random.random(3))

print("*** Three random values (normal distribution, mean 0, standard deviation 1)")
check(np.random.normal(loc=0, scale=1, size=3))

print("*** Three random values (discrete uniform distribution)")
check(np.random.randint(low=1, high=11, size=3))

print("*** Identity matrix 3")
check(np.eye(3))

print("*** An uninitialized array sized 5")
check(np.empty(5, int))
