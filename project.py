import pandas as pd
aapl = pd.read_csv("AAPL.csv")
print(aapl)
print(aapl.describe())
print(aapl.dtypes)
print(aapl.head())
import requests
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=aapl&apikey=CJW6S4N6QQGYGWPZ'
r = requests.get(url)
company_overview = r.json()

print(company_overview)