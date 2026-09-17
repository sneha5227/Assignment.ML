import numpy as np

arr = np.arange(1, 11)

# Normal slice
a = arr[2:6]

# Copy of the slice
b = arr[2:6].copy()

# Change first element of each
a[0] = 999
b[0] = 999

print("Slice:", a)
print("Copy:", b)
print("Original array:", arr)

# A normal slice is a VIEW of the original array,
# so changing a also changes arr.
# .copy() creates a separate copy,
# so changing b does not affect arr.