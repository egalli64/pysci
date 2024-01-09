"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple histogram with dates
"""
from datetime import date, timedelta
import random
import matplotlib.pyplot as plt


first = date(2019, 3, 1)
last = date(2019, 4, 1)
days = (last - first).days
sample = [first + timedelta(days=random.randint(0, days)) for _ in range(600)]

plt.figure(figsize=(12, 6))
plt.hist(sample, bins=days + 1, edgecolor="black")
plt.show()
