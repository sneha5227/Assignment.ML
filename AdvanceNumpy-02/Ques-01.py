import numpy as np

marks = np.array([
    [88, 96, 95],
    [72, 99, 91],
    [98, 85, 97],
    [60, 75, 80]
])

new_marks = marks + np.array([5, 2, 8])
capped_count = np.sum(new_marks > 100)
new_marks = np.minimum(new_marks, 100)

print("Final marks:")
print(new_marks)

print("Number of marks capped:", capped_count)
