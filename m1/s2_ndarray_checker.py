"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

A utility function to check a NumPy array
"""
import numpy as np


def check(a: np.ndarray) -> None:
    """Some basic info on the passed array"""
    print(f"{a} is a {a.ndim}-dimension {a.dtype} {type(a)}", end=" ")
    print(f"with {a.size} elements,", end=" ")
    print(f"total byte size is {a.nbytes},", end=" ")
    print(f"shaped {a.shape}")
