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
print("Original and slices are all working on the same memory:", a)

tail_3_copy = a[-3:].copy()
print("Tail (copy):", tail_3_copy)

a[7] -= 20
print("A copy is not affected by changes on the original:", tail_3_copy)

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
