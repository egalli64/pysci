import numpy as np

a1 = [x for x in range(1, 11)]
print(a1)
print(len(a1))

a2 = np.arange(1, 11)
print(a2)
print(f"{a2.ndim} dimension(s), base type {a2.dtype}, size {a2.size}, shape {a2.shape}")

b1 = [x / 10 for x in range(10, 21)]
print(b1)

b2 = np.arange(1.0, 2.1, 0.1)
print(b2, b2.dtype)

b3 = np.array(b1)
print(b3, b3.dtype)

# passing the required base type to the ctor
b4 = np.array(b1, np.float32)
print(b4, b4.dtype)

c1 = [0] * 10
print(c1)

c2 = np.zeros(10, np.int32)
print(c2)

d = np.zeros((2, 5))
print(d, d.dtype)

e = np.ones((3, 3), np.int32)
print(e)

f = np.random.random((4, 3))
print(f)
