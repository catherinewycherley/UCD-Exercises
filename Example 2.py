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

print(aapl.head())
print(aapl.tail())

print(aapl.describe())

print(aapl.dtypes)


aapl["Date"] = pd.to_datetime(aapl["Date"])
print(aapl.info())


missing_values_count = aapl.isnull().sum()
print(missing_values_count[0:8])

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
avg_price=cleaned_data.groupby("Close").mean()
print(avg_price)


mask_closeprice = cleaned_data.Close > 100
high_price = cleaned_data.loc[mask_closeprice]
print(high_price)

mask_closeprice = cleaned_data.Close > 100
mask_volume = cleaned_data.Volume > 300000000
millionhigh_price_volume = cleaned_data.loc[mask_closeprice & mask_volume]

print(millionhigh_price_volume)



plt.figure(figsize=(10, 8))
cleaned_data['Change'].plot()
plt.xlabel('DATE')
plt.ylabel('PRICE')
plt.title('Change of Apple Stock')
plt.show()


msft = pd.read_csv("MSFT-stock.csv")

print(msft)


msft["Date"] = pd.to_datetime(msft["Date"])
print(msft.info())

msft.set_index(keys='Date', inplace=True)
print(msft.head())



for i in msft:
    print (i)

    for ind, row in msft.iterrows():
        msft.loc[ind, [" Share Price Change"]] = row['Close'] - row['Open']
        print(msft.head())





aapl_msft=cleaned_data.merge(msft, on='Date', suffixes=('_aapl', '_msft'))

print(aapl_msft.head(5))
print (aapl_msft.tail(5))
print(aapl_msft)


aapl_msft.plot(x = 'Date', y = ['Close_aapl', 'Close_msft'], kind='line', title= "Comparison of Apple & Microsoft Closing Stock")
plt.show()

cleaned_data.set_index(keys='Date', inplace=True)


aapl_2020 = cleaned_data.loc['2020']
aapl_2020 = aapl_2020.sort_index(ascending=True)
print(aapl_2020)




def calculate_pe_ratio(closing_price, month):
    if month >= 1 and month < 3:
        earnings = 1.00
    elif month >= 3 and month < 6:
        earnings = 0.9
    elif month >= 6 and month < 9:
        earnings = 0.8
    else:
        earnings = 0.9
    return closing_price / earnings / 4




aapl_2020['pe_ratio'] =np.vectorize(calculate_pe_ratio)(aapl_2020['Close'], aapl_2020.index.month)

print(aapl_2020)

plt.figure(figsize=(10, 8))
aapl_2020['pe_ratio'].plot()
plt.xlabel('DATE')
plt.ylabel('PE RATIO')
plt.title('PE Ratio of Apple Stock in 2020')
plt.show()