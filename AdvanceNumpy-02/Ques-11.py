import numpy as np

s1 = np.array([12, 15, 11, 19, 14])
s2 = np.array([22, 18, 25, 21, 20])
s3 = np.array([31, 35, 29, 33, 30])

# Each sensor as a row
row_stack = np.vstack((s1, s2, s3))

# Each sensor as a column
col_stack = np.column_stack((s1, s2, s3))

print("Sensors as rows:")
print(row_stack)

print("Shape:", row_stack.shape)

print("\nSensors as columns:")
print(col_stack)

print("Shape:", col_stack.shape)

print("\nAre they transpose of each other?")
print(np.array_equal(row_stack.T, col_stack))