"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Factories for ndarray
"""
import numpy as np

a_zeros = np.zeros(6)
print(f"All-zero {a_zeros.dtype} {type(a_zeros)} shaped {a_zeros.shape}:", a_zeros)

a_ones = np.ones((3, 2), dtype=int)
print(f"All-one {a_ones.dtype} {type(a_ones)} shaped {a_ones.shape}:\n", a_ones)

m_full = np.full((2, 2, 2), 42, int)
print(f"All-42 {m_full.dtype} {type(m_full)} shaped {m_full.shape}:\n", m_full)

a_ranged_x = np.array(range(2, 11, 2))
print(f"Ranged {a_ranged_x.dtype} array:", a_ranged_x)

a_ranged = np.arange(2, 11, 2)
print(f"Ranged {a_ranged.dtype} array:", a_ranged)

a_ranged_f = np.arange(1.0, 1.51, 0.1)
print(f"Ranged {a_ranged_f.dtype} array:", a_ranged_f)

a_lin = np.linspace(2, 10, 5, dtype=int)
print(f"Linearly spaced {a_lin.dtype} array:", a_lin)

a_lin_f = np.linspace(1.0, 1.5, 6)
print(f"Linearly spaced {a_lin_f.dtype} array:", a_lin_f)

a_log = np.logspace(0, 2, 5)
print(f"Logarithmically spaced array:", a_log)

a_rand = np.random.random(3)
print("Random (uniform distribution) array:", a_rand)

a_normal = np.random.normal(loc=0, scale=1, size=3)
print("Random (normal distribution) array:", a_normal)

a_randint = np.random.randint(low=1, high=11, size=3)
print("Random integer in [1, 10] array:", a_randint)

m_id = np.eye(3)
print(f"Identity matrix shaped {m_id.shape}:\n", m_id)

a_uninit = np.empty(5, int)
print("An uninitialized array:", a_uninit)
