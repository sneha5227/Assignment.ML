import numpy as np

a = np.array([2, 3, 4])

table = a.reshape(3, 1) * a

print(table) 