"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple bar chart on pandas DataFrame columns
Requires iris.csv from https://github.com/mwaskom/seaborn-data
"""
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("data/iris.csv")
data = iris.groupby("species")["sepal_length"].mean()
plt.bar(data.index, data.values)

plt.xlabel("Species")
plt.ylabel("Average Sepal Length")
plt.title("Average Sepal Length for Each Species")
plt.show()
