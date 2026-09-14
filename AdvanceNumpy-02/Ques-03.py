import numpy as np

arr = np.arange(30)

result = arr.reshape(5, -1).T

# Prediction: shape will be (6, 5)

print("Shape:", result.shape)

# np.arange(30).reshape(4, -1) fails because
# 30 elements cannot be evenly divided into 4 rows.