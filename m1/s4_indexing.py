"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array indexing
"""
import numpy as np

single_throw = np.random.randint(1, 7, size=3)
print("Single throw:", single_throw)
print(f"First die is {single_throw[0]}, last one is {single_throw[-1]}")

two_throws = np.random.randint(1, 7, size=(2, 3))
print("Two throws:\n", two_throws)

print("First and last die in the first throw:", two_throws[0, 0], two_throws[0, -1])
print("First and last die in the last throw:", two_throws[-1, 0], two_throws[-1, -1])

# change a single element values in an array
two_throws[0, 1] = 10
two_throws[1, 1] += 10
two_throws[-1, 0] = 7.5  # can't change data type - truncate!
print("Two throws now are:\n", two_throws)
