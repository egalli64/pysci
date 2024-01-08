"""
Python and Science

https://github.com/egalli64/pysci

Module 3 - pandas

DataFrame
"""
import pandas as pd
import numpy as np

data = {
    "state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
    "year": [2000, 2001, 2002, 2001, 2002, 2003],
    "population": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2],
}
df = pd.DataFrame(data)

print("A data frame")
print(df)

populations = {
    "Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
    "Nevada": {2001: 2.4, 2002: 2.9},
}

dfp = pd.DataFrame(populations)
print("\nA data frame from a nested dictionary")
print(dfp)

print("\nData frame head (five, default)")
print(df.head())

print("\nData frame tail (three)")
print(df.tail(3))

print("\nA data frame with ordered columns (one of them with missing values)")
df2 = pd.DataFrame(data, columns=["year", "state", "population", "debt"])
print(df2)

print("\nColumn extraction /1")
print(df["population"])

print("\nColumn extraction /2")
print(df["state"])

print("\nAssigning a value to an entire column")
df2["debt"] = 42
print(df2)

print("\nAssigning a value to an entire column")
df2["debt"] = 42
print(df2)

print("\nAssigning an arange to an entire column")
df2["debt"] = np.arange(6)
print(df2)

print("\nAssigning a series to a column")
df2["debt"] = pd.Series([-1.2, -1.5, -1.7], index=[2, 4, 5])
print(df2)

print()
df.info()