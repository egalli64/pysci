"""
Python and Science

https://github.com/egalli64/pysci

Module X - Data Analysis

Exploratory Data Analysis - Descriptive Statistics
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("data/cars.csv")
print(df.head(), "\n")

print("Correlation:")
corr_df = df[["bore", "stroke", "compression-ratio", "horsepower"]].corr()
print(corr_df)
print("---\n")

print("correlation between engine-size and price:")
print(df[["engine-size", "price"]].corr())

# Positive Linear Relationship
sns.regplot(x="engine-size", y="price", data=df)
plt.show()

# Negative relationship
sns.regplot(x="highway-mpg", y="price", data=df)
plt.show()

print("---")
print("correlation between highway-mpg and price:")
print(df[["highway-mpg", "price"]].corr())

# Weak Linear Relationship
sns.regplot(x="peak-rpm", y="price", data=df)
plt.show()

print("---")
print("correlation between stroke and price:")
print(df[["stroke", "price"]].corr())

# Categorical Variables

print("\nOverlapping -> not good predictor")
sns.boxplot(x="body-style", y="price", data=df)
plt.show()

print("\nDistinct -> potential good predictor")
sns.boxplot(x="engine-location", y="price", data=df)
plt.show()
