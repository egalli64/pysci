"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

A utility function to check a NumPy array
"""

import numpy as np


def check(a: np.ndarray) -> None:
    """Some basic info on the passed ndarray"""
    try:
        print(a, "is ", end="")
        print(f"a\n\t{a.ndim}-dimension {a.dtype} {type(a)} (type size {a.dtype.itemsize} byte)")
        print(f"\twith {a.size} elements,", end=" ")
        print(f"shaped {a.shape}", end=" ")
        print(f"total byte size is {a.nbytes}")
    except AttributeError:
        print("not an ndarray")


if __name__ == "__main__":
    check(None)
