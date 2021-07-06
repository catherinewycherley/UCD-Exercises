import pandas as pd
import numpy as np
import requests
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



aapl['Change'] = aapl['Close'] - aapl['Open']
print(aapl)

mask_closeprice = aapl.Close > 100
high_price = aapl.loc[mask_closeprice]
print(high_price)

mask_closeprice = aapl.Close > 100
mask_volume = aapl.Volume > 300000000
millionhigh_price_volume = aapl.loc[mask_closeprice & mask_volume]

print(millionhigh_price_volume)

import matplotlib.pyplot as plt

print(aapl.sort_values("Change"))

new_appl=aapl.dropna()
print(new_appl)

print(new_appl.sort_values("Change"))

print(aapl.head())
print(aapl.shape)

missing_values_count = aapl.isnull().sum()
print(missing_values_count[0:5])

droprows= aapl.dropna()

print(aapl.shape,droprows.shape)


dropcolumns = aapl.dropna(axis=1)
print(aapl.shape,dropcolumns.shape)

cleaned_data = aapl.fillna(0)
print(cleaned_data)



drop_duplicates= aapl.drop_duplicates()
print(aapl.shape,drop_duplicates.shape)

print(aapl['Close'].max())
print(aapl['Close'].min())

aapl1 = aapl.iloc[:,0]
print(aapl1.tail())


plt.figure(figsize=(10, 8))
aapl['Close'].plot()
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Closing price of Apple Stock')
plt.show()

aapl['PriceDiff'] = aapl['Close'].shift(-1) - aapl['Close']
print(aapl['PriceDiff'])

aapl['Return'] = aapl['PriceDiff'] /aapl['Close']
print(aapl['Return'])



aapl['ma50'] = aapl['Close'].rolling(50).mean()


plt.figure(figsize=(10, 8))
aapl['ma50'].plot(label='MA50')
aapl['Close'].plot(label='Close')
plt.legend()
plt.show()

aapl['MA10'] = aapl['Close'].rolling(10).mean()
aapl['MA50'] = aapl['Close'].rolling(50).mean()
aapl = aapl.dropna()
print(aapl.head())

microsoft = pd.read_csv("Microsoft_data.csv")

print(microsoft)


microsoft["Date"] = pd.to_datetime(microsoft["Date"])
print(microsoft.info())

microsoft.set_index(keys='Date', inplace=True)
print(microsoft.head())

aapl_microsoft=aapl.merge(microsoft, on='Date', suffixes=('_aapl', '_microsoft'))

print(aapl_microsoft.head(5))


plt.figure(figsize=(15, 8))
aapl['Volume'].plot()
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('volume of Apple Stock')
plt.show()

import matplotlib.pyplot as plt

aapl.plot(y=["High", "Low",])
plt.show()

def calculate_pe_ratio(closing_price, month):
    if month >= 1 and month < 4:
        earnings = 1.10
    elif month >= 4 and month < 7:
        earnings = 0.68
    elif month >= 7 and month < 10:
        earnings = 0.59
    else:
        earnings = 0.78
    return closing_price / earnings / 4


aapl_2020['pe_ratio'] =np.vectorize(calculate_pe_ratio)(aapl_2020['Close'], aapl_2020.index.month)

print(aapl_2020)


