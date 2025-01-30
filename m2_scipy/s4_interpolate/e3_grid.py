"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Interpolation - N-D - RegularGridInterpolator
"""

import numpy as np
from scipy.interpolate import RegularGridInterpolator


def func(u, v):
    """The 2D function that we want to interpolate"""
    return u * np.cos(u * v) + v * np.sin(u * v)


# assuming we know only some points
fit_points = [np.linspace(0, 3, 8), np.linspace(0, 3, 11)]
values = func(*np.meshgrid(*fit_points, indexing="ij"))

# to evaluate the interpolation
coordinates = np.meshgrid(np.linspace(0, 3, 80), np.linspace(0, 3, 80), indexing="ij")

true_values = func(*coordinates)
print(true_values[1], "row 1 of true values")
print()

test_points = np.array([coordinates[0].ravel(), coordinates[1].ravel()]).T

# linear interpolation
interpolator = RegularGridInterpolator(fit_points, values)
linear = interpolator(test_points).reshape(80, 80)
print(linear[1], "row 1 of linear interpolation")
