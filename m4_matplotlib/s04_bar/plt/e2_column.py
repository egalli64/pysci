"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple bar chart from a DataFrame column
Requires iris.csv from https://github.com/mwaskom/seaborn-data
"""
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("data/iris.csv")
sample = iris.sample(100)

data = sample["species"].value_counts()
plt.bar(data.index, data.values)

plt.xlabel("Species")
plt.ylabel("Count")
plt.title("Bar Chart for Iris Species in random sample")
plt.show()
