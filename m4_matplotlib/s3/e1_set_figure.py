"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Some figure settings
"""
import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-2 * np.pi, 2 * np.pi, 200)

# set the figure before working on it
plt.figure(figsize=(10, 5), facecolor="lightyellow")

plt.title("A more descriptive figure")
plt.xlabel("X axis")
plt.ylabel("Y axis")

# labels are put in legend
plt.plot(xs, np.sin(xs), label="sin(x)")
plt.plot(xs, (lambda x: x**2 - 20)(xs), label="x^2")

plt.axvline(x=5, color="r", linestyle="--", label="Vertical Line")
plt.axhline(y=5, color="g", linestyle="-.", label="Horizontal Line")
plt.legend()

plt.grid(True)
plt.xlim(0, 6)
plt.ylim(-20, 20)

plt.xticks(np.arange(0, 7))
plt.yticks(np.arange(-20, 21, 5))

plt.annotate(
    "We are here",
    xy=(5, 5),
    xytext=(3.8, 10),
    arrowprops=dict(shrink=0.05, width=1, headwidth=7),
)

plt.show()
