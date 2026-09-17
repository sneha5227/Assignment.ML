import numpy as np

# 4x4 matrix
matrix = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Role 1: Extract diagonal
diagonal = np.diag(matrix)

print("Original matrix:")
print(matrix)

print("\nDiagonal:")
print(diagonal)

# Role 2: Create a diagonal matrix from a 1D array
arr = np.array([10, 20, 30, 40])

diagonal_matrix = np.diag(arr)

print("\n1D array:")
print(arr)

print("\nDiagonal matrix:")
print(diagonal_matrix)