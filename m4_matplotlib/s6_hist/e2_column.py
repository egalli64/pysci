"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple histogram from a DataFrame column
Requires iris.csv from https://github.com/mwaskom/seaborn-data
"""
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("data/iris.csv")
plt.hist(iris["sepal_length"], edgecolor="black")

plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Histogram for Iris Sepal Length")
plt.show()
