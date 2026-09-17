import numpy as np

marks = np.array([
    [45, 28, 67, 80],
    [33, 90, 55, 41],
    [72, 66, 30, 58],
    [88, 79, 91, 84],
    [25, 40, 38, 52]
])

# Replace marks below 35 with 35
marks[marks < 35] = 35

# Calculate total marks of each student
totals = marks.sum(axis=1)

# Find the index of the topper
topper_index = np.argmax(totals)

# Get topper's total
topper_total = totals[topper_index]

print("Updated marks:")
print(marks)

print("Student totals:")
print(totals)

print("Topper index:", topper_index)
print("Topper total:", topper_total)