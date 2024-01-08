"""
Python and Science

https://github.com/egalli64/pysci

Module 3 - pandas

Series
"""
import pandas as pd

# from list to series
ps = pd.Series([42, 99, 51, 27])
print("A pandas series:", ps, sep="\n")
print(f"\nIt is a {type(ps)} with dtype {ps.dtype}\n")
print("The associated array is:\n", ps.array, "\n")
print("The associated index is:", ps.index)

# from two lists (values and indices) to series
ps2 = pd.Series([24, 99, 15, 72], ["a", "b", "c", "d"])
print("\nAnother pandas series:", ps2, sep="\n")
print("\nThe associated index is:", ps2.index)

# accessing an element
print("\nElement 'b' is", ps2["b"])

# extracting a slice
ps3 = ps2[["c", "a", "d"]]
print("\nA slice of ps2:", ps3, sep="\n")

# operating a transformation
ps4 = ps3 * 2
print("\nDoubling ps3:", ps4, sep="\n")

# from dictionary to series
a_dict = {"a": 42, "b": 76, "c": 87, "d": 43}
ps5 = pd.Series(a_dict)
print("\nA pandas series from a dictionary:", ps5, sep="\n")

# from series to dictionary
b_dict = ps4.to_dict()
print("\nA pandas series converted to dictionary:", b_dict)

# operator-in on a series
print("\nIs index 'c' available in ps4?", "c" in ps4)
