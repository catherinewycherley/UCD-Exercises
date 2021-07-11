import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns


url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=aapl&apikey=CJW6S4N6QQGYGWPZ'
r = requests.get(url)
company_overview = r.json()

print(company_overview)

aapl = pd.read_csv("AAPL.csv")
print(aapl)
print(aapl.head())
print(aapl.tail())

print(aapl.describe())

print(aapl.dtypes)

print(aapl.describe())

aapl["Date"] = pd.to_datetime(aapl["Date"])
print(aapl.info())

aapl.set_index(keys='Date', inplace=True)


print(aapl.head())

aapl_2020 = aapl.loc['2020']
aapl_2020 = aapl_2020.sort_index(ascending=True)
print(aapl_2020)

Column_List = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']


aapl.plot(x = "Date", y = Column_List, subplots = True, layout = (3, 3), figsize = (15, 15), sharex = False, title = "Apple Stock Value Trend from 1980 - 2020", rot = 90)
plt.show()


