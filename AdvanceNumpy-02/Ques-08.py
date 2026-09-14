import numpy as np

X = np.array([
    [50, 1200, 3],
    [80, 1500, 9],
    [65, 900, 5],
    [95, 2000, 7]
])

col_min = X.min(axis=0)
col_max = X.max(axis=0)

normalized = (X - col_min) / (col_max - col_min) # formula

print("Normalized matrix:")
print(normalized)

print("Column minimums:", normalized.min(axis=0))
print("Column maximums:", normalized.max(axis=0))