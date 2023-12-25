"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array - concatenate
"""
import numpy as np

a1 = np.arange(3)
a2 = np.arange(3, 6)
print("Two arrays:", a1, a2)

# from two arrays to a new, joined, array
ac = np.concatenate((a1, a2))
print("Array concatenation:", ac)
print("Concatenating array and iterable:", np.concatenate((a1, (8, 11, 23))))

# "append" a single value to an array (not in-place)
ac = np.append(ac, 42)
print("Append (concatenate) a single value:", ac)

ac = np.append(ac, (18, 27))
print("Append (concatenate) more values:", ac)

m1 = np.array(((1, 2, 3), (3, 4, 5)))
m2 = np.array([[5, 6, 7], [7, 8, 9]])
print(f"\nTwo dimensional arrays:\n{m1}\n{m2}")

# vertical concatenation
print("Stack them vertically ...")
print(np.concatenate((m1, m2)), "by concatenate, implicitly vertical")
print(np.concatenate((m1, m2), axis=0), "by concatenate, explicitly vertical")
print(np.vstack((m1, m2)), "by vstack\n")

print(np.vstack((a1, m1)), "vstack a one-dimensional array and a bi-dimensional one\n")

# horizontal concatenation
print(np.concatenate((m1, m2), axis=1), "horizontal concatenation")
print(np.hstack((m1, m2)), "hstack\n")

column = np.array([[7], [8]])
print(column, "a column, shaped", column.shape)
print(np.hstack((m1, column)), "hstack a column and a bi-dimensional array")
