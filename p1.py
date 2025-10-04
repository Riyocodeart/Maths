import pandas as pd

df = pd.read_csv("healthcare-dataset-stroke-data.csv")
ages = df['age'].dropna()
print("mean:",ages.mean())
print("median",ages.median())
print("mode:",ages.mode().tolist())
