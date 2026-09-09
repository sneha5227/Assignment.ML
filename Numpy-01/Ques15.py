import numpy as np
marks = np.array([56, 91, 44, 77, 62, 85, 39, 70])
print(marks[marks > 60])
print(marks[(marks >= 50) & (marks <= 80)])