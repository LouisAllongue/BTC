import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime

start_date = '2018-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')

sp500 = yf.download('^GSPC', start=start_date, end=end_date)['Close']
btc = yf.download('BTC-USD', start=start_date, end=end_date)['Close']


data = sp500.join(btc, how = 'inner')
data.dropna(inplace=True)

data_norm = data / data.iloc[0] * 100
data_norm.columns = ['sp500', 'btc']

data = data_norm.copy()
data['sp500'] = data['sp500'].astype(float)
data['btc'] = data['btc'].astype(float)
data = data.reset_index()

plt.figure(figsize=(14, 7))
plt.plot(data.index, data['sp500'], label='S&P 500', color='blue')
plt.plot(data.index, data['btc'], label='Bitcoin', color='orange')
plt.title('S&P 500 vs Bitcoin Price Normalized to 100')
plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.legend()
plt.grid()
plt.show()

