import numpy as np

m = np.array([
    [4, 8, 15],
    [16, 23, 42]
])

# Create 1D arrays
flat = m.flatten()
rav = m.ravel()

# Change first element
flat[0] = 100
rav[0] = 200

print("Flatten array:")
print(flat)

print("Ravel array:")
print(rav)

print("Original matrix:")
print(m)

# Difference:
# flatten() creates a COPY, so changing flat does NOT change m.
# ravel() usually creates a VIEW, so changing rav DOES change m.