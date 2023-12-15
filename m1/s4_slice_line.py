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

# NumPy slices are views
rest_5[2] += 20
print("Changes in a slice are reflected in the orginal array:", a)

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
