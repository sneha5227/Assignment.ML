import numpy as np

# Create two random 3x3 matrices
np.random.seed(7)

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

# Matrix multiplication
AB = A @ B
BA = B @ A

# Check whether both results are equal
same = np.array_equal(AB, BA)

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nA @ B:")
print(AB)

print("\nB @ A:")
print(BA)

print("\nAre A @ B and B @ A equal?")
print(same)

# Conclusion:
# Matrix multiplication is NOT commutative in general.
# That means A @ B is usually NOT equal to B @ A.