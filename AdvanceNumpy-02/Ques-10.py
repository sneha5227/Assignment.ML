import numpy as np

m = np.array([
    [10, 80, 45],
    [55, 20, 99],
    [70, 33, 12]
])

rows, cols = np.where(m > 50)

print("Row indices:", rows)
print("Column indices:", cols)

print("Elements greater than 50:", m[rows, cols])

m_copy = m.copy()
m_copy[rows, cols] = 0

print("Original matrix:")
print(m)

print("Modified copy:")
print(m_copy)