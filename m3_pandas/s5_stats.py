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

# when not interested in stats on species
iris_nums = iris.drop("species", axis=1)

# make the dataset a bit dirty
iris.loc[0, "sepal_width"] = np.nan
iris.loc[2, "petal_width"] = np.nan
iris.loc[4, "sepal_length"] = np.nan

print("Describing the iris dataset")
print(iris.head())
print(iris.describe())

print("\nMean values")
print(iris_nums.mean())
print("\nMedian values")
print(iris_nums.median())
print("\nStandard deviation")
print(iris_nums.std())
print("\nVariance")
print(iris_nums.var())

print("\nSum values")
print(iris_nums.sum())
print("\nMin values")
print(iris.min())
print("\nMax values")
print(iris.max())

print("\nCount non-missing values")
print(iris.count())

print("\nCount unique values")
print(iris.nunique())

print("\nReturn unique values in species")
print(iris["species"].unique())
