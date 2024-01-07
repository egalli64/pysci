"""
Python and Science

https://github.com/egalli64/pysci

Module 3 - Matplotlib

Draw a first bar chart
"""
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
plt.bar(tips['day'], tips['total_bill'])
plt.show()
