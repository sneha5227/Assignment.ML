import numpy as np

np.random.seed(1)

m = np.random.randint(1, 101, size=(6, 6))

print("Random matrix:")
print(m)

row_max = m.max(axis=1)
col_min = m.min(axis=0)

print("Row-wise maximum:")
print(row_max)

print("Column-wise minimum:")
print(col_min)
