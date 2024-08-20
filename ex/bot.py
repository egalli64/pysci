"""
Python and Science

https://github.com/egalli64/pysci

Examples
"""

import pandas as pd
import matplotlib.pyplot as plt

# put in here the chosen base date
base_date = pd.to_datetime("2024-08-20")

# read from a CSV containing name,price,end_date for each BOT considered
df = pd.read_csv("data/bot.csv")
df["end_date"] = pd.to_datetime(df["end_date"])

plt.figure()

for row in df.itertuples(index=False):
    delta = (row.end_date - base_date).days
    pct = ((100 / row.price) - 1) * (365 / delta)
    plus = 1_000 * (pct * delta / 365)

    plt.plot(
        [base_date, row.end_date],
        [row.price, 100],
        marker="o",
        label=f"{row.name} ({pct:.2%}, {plus:.2f})",
    )

plt.ylabel("Price")
plt.title("BOT")
plt.grid(True)

plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
