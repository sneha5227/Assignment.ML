import numpy as np

heights = np.array([172, 158, 181, 166])
weights = np.array([68, 52, 84, 59])

result = np.hstack((heights, weights))
print(result)
print("Shape:", result.shape)

# hstack joins the two 1D arrays side-by-side into one long 1D array,
# so it does not create two columns.
table = np.column_stack((heights, weights))
print(table)
print("Shape:", table.shape)