"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple pie chart from a DataFrame column
Requires iris.csv from https://github.com/mwaskom/seaborn-data
"""
import matplotlib.pyplot as plt
import pandas as pd

sample = pd.read_csv("data/iris.csv").sample(97)
data = sample["species"].value_counts()
plt.pie(data.values, labels=data.index, autopct="%.2f%%")

plt.title("Pie Chart of Iris Species  in random sample")
plt.show()
