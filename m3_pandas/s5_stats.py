"""
Python and Science

https://github.com/egalli64/pysci

Module 3 - pandas

Some stats
Requires iris.csv from https://github.com/mwaskom/seaborn-data
"""
import pandas as pd
import numpy as np

iris = pd.read_csv("data/iris.csv")

# make the dataset a bit dirty
iris.loc[0, "sepal_width"] = np.nan
iris.loc[2, "petal_width"] = np.nan
iris.loc[4, "sepal_length"] = np.nan

# when not interested in stats on species
iris_nums = iris.drop("species", axis=1)
# when interested in petal width only
pw_col = iris["petal_width"]

print("Describing the iris dataset")
print(iris.head())
print(iris.describe())

print("\nDescribing the petal width iris column")
print(pw_col.head())
print(pw_col.describe())

print("\nMean values")
print(iris_nums.mean())
print("petal width only:", pw_col.mean())

print("\nMedian values")
print(iris_nums.median())
print("petal width only:", pw_col.median())

print("\nStandard deviation")
print(iris_nums.std())
print("petal width only:", pw_col.std())

print("\nVariance")
print(iris_nums.var())
print("petal width only:", pw_col.var())

print("\nSum values")
print(iris_nums.sum())
print("petal width only:", pw_col.sum())

print("\nMin values")
print(iris.min())
print("petal width only:", pw_col.min())

print("\nMax values")
print(iris.max())
print("petal width only:", pw_col.max())

print("\nCount non-missing values")
print(iris.count())
print("petal width only:", pw_col.count())

print("\nCount unique values")
print(iris.nunique())
print("petal width only:", pw_col.nunique())

print("\nReturn unique values in species")
print(iris["species"].unique())

print("\nReturn count values for species")
print(iris["species"].value_counts())

print("\nReturn count values for iris")
print(iris.value_counts())
