import numpy as np
a = np.array([2,4,6])
b = np.array([2.0, 4.0, 6.0])

print(a.dtype)
print(b.dtype)

b = b.astype(int)

print("New b:", b)
print("New b dtype:", b.dtype)
