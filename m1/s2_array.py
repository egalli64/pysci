"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

The ndarray
"""
import numpy as np

print("Introducing NumPy version", np.__version__)

# a native list (of anything)
list = [x for x in range(3)]
list.append("42")
print("A native Python list:", list)

if isinstance(list[-1], str):
    # example with native array
    from array import array

    # arrays are homogeneous, comment next line to get a TypeError
    del list[-1]

    # a native int array
    native_array = array("i", list)
    print("A native Python array:", native_array)

# NumPy integer ndarray (homogeneous)
a = np.array([1, 2, 3])
print(f"An {a.dtype} {type(a)} sized {a.size}: {a}")

# NumPy tries to understand which type use for array
a2 = np.array([1, 2, 10 / 3])
print(f"A {a2.dtype} {type(a2)}: {a2}")

# requiring a base type
a3 = np.array([1, 2, 3], dtype=float)
print(f"Another {a3.dtype} {type(a3)}: {a3}")

# matrices
m1 = np.array([range(i, i + 3) for i in range(3)])
print(f"An {m1.dtype} {type(m1)} matrix shaped {m1.shape}:\n", m1)

m2 = np.array([[1, 2], [3, 4], [5, 6]])
print(f"An {m2.dtype} {type(m2)} matrix shaped {m2.shape}:\n", m2)

m3 = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex)
print(f"A {m3.dtype} {type(m3)} matrix shaped {m3.shape}:\n", m3)
