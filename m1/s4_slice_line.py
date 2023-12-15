"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array slicing
"""
import numpy as np

a = np.arange(10)
print("An array:", a)

head_5 = a[:5]
print("Head:", head_5)

rest_5 = a[5:]
print("The rest:", rest_5)

center = a[3:-3]
print("The central part:", center)

alt_0 = a[::2]
print("Alternate from 0:", alt_0)

alt_1 = a[1::2]
print("Alternate from 1:", alt_1)

reversed = a[::-1]
print("Reversed:", reversed)

reversed_alt = a[::-2]
print("Reversed alternate:", reversed_alt)

# multi dim
m = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
print("A matrix:\n", m)
