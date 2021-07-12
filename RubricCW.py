import pandas as pd
import numpy as np
import requests

import matplotlib.pyplot as plt

plt.style.use('dark_background')


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



aapl["Date"] = pd.to_datetime(aapl["Date"])
print(aapl.info())


missing_values_count = aapl.isnull().sum()
print(missing_values_count[0:7])

droprows= aapl.dropna()

print(aapl.shape,droprows.shape)

dropcolumns = aapl.dropna(axis=1)
print(aapl.shape,dropcolumns.shape)

cleaned_data = aapl.fillna(0)
print(cleaned_data)


Column_List = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

for x in Column_List:
    print (x)



cleaned_data.plot(x = "Date", y = Column_List, subplots = True, layout = (3, 3), figsize = (20, 20), sharex = False, title = " Trend of Apple Stock Value from 1980 - 2020", rot = 90)
plt.show()



cleaned_data['Change'] = cleaned_data['Close'] - cleaned_data['Open']
print(cleaned_data)

print(cleaned_data.sort_values("Change"))
cleaned_data1 = cleaned_data.iloc[:,1]
print(cleaned_data1)

avg_price=cleaned_data.groupby("Close").mean()
print(avg_price)
