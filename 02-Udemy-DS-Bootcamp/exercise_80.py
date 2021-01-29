
# Paul A. Beata
# January 28, 2021

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data contains the prices of three stocks: AAPL, GOOGL, BAC
data = pd.read_csv('./data/stock_data.csv')
print(data)


# Task 1
# Create a scatter plot for the Apple and Google stock prices
plt.figure()
plt.plot(data['AAPL'], data['GOOGL'], 'bo')
plt.xlabel('Stock Price of Apple')
plt.ylabel('Stock Price of Google')


# Task 2
# Create a scatter plot for the Apple and Bank of America stock prices
plt.figure()
plt.plot(data['AAPL'], data['BAC'], 'ro')
plt.xlabel('Stock Price of Apple')
plt.ylabel('Stock Price of Bank of America')

plt.xticks(np.arange(0, 170, 20))
plt.yticks(np.arange(20, 32, 2))


# display the plots
plt.show()
