import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8, 9],
    [1, 0, 2]
])

result1 = A @ B.T # A is (2,3) and B.T is (3,2), so multiplication is legal.
result2 = A.T @ B # A.T is (3,2) and B is (2,3), so multiplication is legal.

print("A @ B.T:")
print(result1)
print("Shape:", result1.shape)

print("\nA.T @ B:")
print(result2)
print("Shape:", result2.shape)

# A @ B is not legal because (2,3) @ (2,3)
# has mismatched inner dimensions: 3 != 2.