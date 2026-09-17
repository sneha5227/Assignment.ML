import numpy as np

np.random.seed(7)

# Generate 28 temperature readings
temps = np.random.randint(15, 41, 28)

# Reshape into 4 weeks and 7 days
weekly_temps = temps.reshape(4, 7)

# Find average temperature of each week
weekly_avg = weekly_temps.mean(axis=1)

# Find the hottest week
hottest_week = np.argmax(weekly_avg)

# Count days where temperature crossed 35°C
hot_days = np.sum(temps > 35)

print("Temperature readings:")
print(temps)

print("\nTemperatures week-wise:")
print(weekly_temps)

print("\nWeekly averages:")
print(weekly_avg)

print("\nHottest week:", hottest_week + 1)
print("Hottest week's average:", weekly_avg[hottest_week])

print("\nNumber of days above 35°C:", hot_days)