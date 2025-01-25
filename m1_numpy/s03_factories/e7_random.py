"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

ndarray random based factory 
"""

import numpy as np

print("Random distributions\n")
print("1D uniform:", np.random.random(3))
print("2D uniform (by shape):")
print(np.random.random((2, 3)))
print("2D uniform (by dimensions):")
print(np.random.rand(2, 3))

print("discrete uniform:", np.random.randint(low=1, high=11, size=3))
print("normal mean 0, standard deviation 1:", np.random.normal(loc=0, scale=1, size=3))
