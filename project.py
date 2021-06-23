import pandas as pd
aapl = pd.read_csv("AAPL.csv")
print(aapl)
print(aapl.describe())
print(aapl.dtypes)
print(aapl.head())
