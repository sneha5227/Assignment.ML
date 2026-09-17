import numpy as np

arr = np.array([10, 20, 30, 40, 50])

minimum = arr.min()
maximum = arr.max()

normalized = (arr - minimum) / (maximum - minimum)

print("Original array:")
print(arr)

print("Minimum:", minimum)
print("Maximum:", maximum)

print("Normalized array:")
print(normalized)