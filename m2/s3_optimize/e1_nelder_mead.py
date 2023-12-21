"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Optimization - minimize - Nelder-Mead
"""
import numpy as np
from scipy.optimize import minimize


def rosen(x):
    return sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)


x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method="nelder-mead", options={"xatol": 1e-8, "disp": True})
print(res)
print("\nThe resulting x is", res.x)
