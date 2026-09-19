import pandas as pd

t = pd.read_csv("Pandas-01/Titanic-Dataset.csv")

print(t.shape)
print(t.info())

# Percentage of missing Age values = 19.87%