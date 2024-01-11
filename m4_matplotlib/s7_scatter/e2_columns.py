"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple scatter plot from DataFrame columns
Requires tips.csv from https://github.com/mwaskom/seaborn-data
"""
import matplotlib.pyplot as plt
import pandas as pd

tips = pd.read_csv("data/tips.csv")
plt.scatter(tips["total_bill"], tips["tip"])

plt.xlabel("Bill")
plt.ylabel("Tip")
plt.title("Scatter Plot for Tips")
plt.show()
