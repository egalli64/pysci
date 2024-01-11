"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

A simple line graph with dates
"""
import pandas as pd
import matplotlib.pyplot as plt

days = pd.date_range(start="2022-01-01", periods=10)
values = [20, 22, 25, 18, 30, 28, 35, 40, 38, 42]

plt.figure(figsize=(12, 6))
plt.plot(days, values, marker=".")
plt.title("A Linear Time Series")
plt.show()
