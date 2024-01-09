"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple pie chart
Requires iris.csv from https://github.com/mwaskom/seaborn-data
"""
import matplotlib.pyplot as plt
import pandas as pd

sample = pd.read_csv("data/iris.csv").sample(97)
species_counts = sample["species"].value_counts()
plt.pie(species_counts.values, labels=species_counts.index, autopct="%.2f%%")

plt.title("Pie Chart of Iris Species")
plt.show()
