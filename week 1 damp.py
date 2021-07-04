print(8/2)
print (2**2)
price = 200
earnings = 5
pe_ratio = price/earnings
print ("Pe_ratio")
print (10+2)
print (10*2)
print (10-7)

revenue_1=50
revenue_2=60
revenue_3=70
total = revenue_1+revenue_2+revenue_3
print (total)
print("total")
average= total/3
print (average)
pe_ratio = 44
print(type(pe_ratio))
print (1==2)
print (1==1)
print (type(1==1))
x=5
print (x*5)
y='stock'
print(y*3)
company_1="Apple"
print (company_1)
year_1=2017
print(year_1)
revenue_4=22698.36
print(revenue_1)
print(revenue_4)
print(type(company_1))
print(type(year_1))
print(type(revenue_4))
test_company='Apple'
print(company_1 == test_company)
print(revenue_1 > revenue_2)
year_1_str=str(year_1)
revenue_4_str=str(revenue_4)
sentence = 'The revenue of'  +    company_1 + ' in' + ' 2017' + ' was' +'  229.23' + ' billion.'
print(sentence)
names = ['Apple Inc', 'Coca-Cola', 'Walmart']
print(names)
prices = [159.54, 37.13, 71.17]
print(names[0])
print(names[1])
print(prices[-1])
names_subset = names[1:]
print(names_subset)
prices_subset = prices[0:3]
print(prices_subset)
cpi=[['Jan','Feb','Mar'],[204.9,256.9,387.6]]
print(cpi[1])
print(cpi[1][0])
stocks = [names, prices]
print(stocks)
print(stocks[1])
print(stocks[0][1])
print(stocks[1][2])
prices.sort()
print(prices)
months=['Jan','feb','Mar']
months.append('apr')
print(months)
months.extend(['may','jun','jul'])
print(months)
calenders=['Jan','feb','Mar']
priceses=[10,20,30]
print(calenders.index('feb'))
print(priceses[1])
min_price=min(prices)
min_index=prices.index(min_price)
min_month=months[min_index]
print(min_month)
import numpy as np
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]
prices_array = np.array(prices)
earnings_array=np.array(earnings)
print(prices_array)
print(earnings_array)
pe_array = prices_array/earnings_array
print(pe_array)
prices_subset_1 = prices_array[0:3]
print((prices_subset_1))
prices_subset_2 = prices_array[-3:]
print(prices_subset_2)
prices_subset_3 = prices_array[0:7:3]
print(prices_subset_3)
stock_array=np.array([prices,earnings])
print(stock_array)
print(stock_array.shape)
print(stock_array.size)
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)
print(stock_array_transposed.shape)
print(stock_array_transposed.size)
prices = stock_array_transposed[:, 0]
print(prices)
arnings = stock_array_transposed[:,1]
print(earnings)
company_1 = stock_array_transposed[0]
print(company_1)
prices_mean = np.mean(prices)
print(prices_mean)
prices_std = np.std(prices)
print(prices_std)
company_ids = np.arange(1, 8, 1)
print(company_ids)
company_ids_odd = np.arange(1, 8, 2)
print(company_ids_odd)
price_mean = np.mean(prices)
boolean_array = (prices > price_mean)
print(boolean_array)
above_avg = prices[boolean_array]
print(above_avg)
days=('Mon', 'Tues', 'Wed', 'Thur')
cost= (10,60,30,10)
import matplotlib.pyplot as plt
plt.plot(days,cost)
plt.show()
plt.plot(days, cost, color="red", linestyle="--")
plt.show()
plt.xlabel('days')
plt.ylabel('cost')
plt.title('Company Stock Prices Over Time')
plt.plot(days,cost)
plt.show()
plt.plot(days,cost)
plt.scatter(days, cost, color='green')
plt.show()
from datetime import datetime
datetime.now()
print(datetime.now())

aapl['Date'] = aapl['Date'].apply(pd.Timestamp)
microsoft['Date'] = microsoft['Date'].apply(pd.Timestamp)
print(aapl.head())
print(microsofr.head())