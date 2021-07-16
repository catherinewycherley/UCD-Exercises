import pandas as pd
import numpy as np
import requests



msft = pd.read_csv("MSFT-stock.csv")



print(msft)



for i in msft:
    print (i)

    for ind, row in msft.iterrows():
        msft.loc[ind, [" Share Price Change"]] = row['Close'] - row['Open']
        print(msft.head())
        break

msft["Date"] = pd.to_datetime(msft["Date"])
print(msft.info())

msft.set_index(keys='Date', inplace=True)




