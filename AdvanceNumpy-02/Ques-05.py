import numpy as np

sales = np.array([120, 135, 98, 160, 175, 190, 88, 92, 105, 210, 198, 230])
Q = sales.reshape(4, 3)

print("Quarterly sales:")
print(Q)

averages = Q.mean(axis=1)

highest_quarter = np.argmax(averages)
highest_average = averages[highest_quarter]

print("Quarter index:", highest_quarter)
print("Highest average sales:", highest_average) 