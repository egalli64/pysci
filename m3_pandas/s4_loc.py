"""
Python and Science

https://github.com/egalli64/pysci

Module 3 - pandas

Accessing data by loc and iloc
Requires iris.csv from https://github.com/mwaskom/seaborn-data
"""

import pandas as pd

iris = pd.read_csv("data/iris.csv")

# using loc
row = iris.loc[0]
print("iris row 0 by loc")
print(row, "\n")
print("accessing petal_length in the row (by loc):", row.loc["petal_length"], "\n")

rows = iris.loc[1:3]
print("iris rows 1 and 2 by loc")
print(rows, "\n")

col = iris.loc[:, "sepal_width"]
print("iris column sepal_width by loc")
print(col, "\n")

chunk = iris.loc[[0, 2], ["sepal_width", "petal_length"]]
print("Sub-table, rows 0 and 2, columns 'sepal_width' and 'petal_length', by loc")
print(chunk, "\n")

cell = iris.loc[2, "sepal_width"]
print("Cell, row 2, column 'sepal_width', by loc")
print(cell, "\n")

# using iloc
row = iris.iloc[0]
print("iris row 0 by iloc")
print(row, "\n")
print("accessing petal_length in the row (by iloc):", row.iloc[2], "\n")

rows = iris.iloc[1:3]
print("iris rows 1 and 2 by iloc")
print(rows, "\n")

col = iris.iloc[:, 1]
print("iris column 1 by iloc")
print(col, "\n")

chunk = iris.iloc[[0, 2], [1, 2]]
print("Sub-table, rows 0 and 2, columns 1 and 2, by iloc")
print(chunk, "\n")

cell = iris.iloc[2, 1]
print("Cell, row 2, column 1, by iloc")
print(cell, "\n")
