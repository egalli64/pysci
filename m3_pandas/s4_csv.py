"""
Python and Science

https://github.com/egalli64/pysci

Module 3 - pandas

Read from CSV (and sample)
Requires iris.csv from https://github.com/mwaskom/seaborn-data
"""

import pandas as pd

# giving numbers as column names to a headerless CSV
iris = pd.read_csv("data/headerless.csv", header=None)
print(iris, "\n")

# giving names to a headerless CSV
iris = pd.read_csv("data/headerless.csv", names=["s_l", "s_w", "p_l", "p_w", "species"])
print(iris, "\n")

# plain access to CSV
iris = pd.read_csv("data/iris.csv")
print("Head of the iris dataset")
print(iris.head(), "\n")

print("sampling 10 rows")
sample = iris.sample(10)
print(sample, "\n")
