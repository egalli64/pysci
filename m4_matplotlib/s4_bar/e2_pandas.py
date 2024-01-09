"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple bar chart
Requires iris.csv from https://github.com/mwaskom/seaborn-data
"""
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("data/iris.csv")
sample = iris.sample(100)

# Count the occurrences of each species in the sample
species_counts = sample["species"].value_counts()

plt.bar(species_counts.index, species_counts.values)

plt.xlabel("Species")
plt.ylabel("Count")
plt.title("Bar Chart of Iris Species")
plt.show()
