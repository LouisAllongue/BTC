from matplotlib import pyplot as plt
import yfinance as yf
from datetime import datetime

start_date = '2018-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')

# Downloading data

btc = yf.download('BTC-USD', start=start_date, end=end_date)['Close']

#Stock
sp500 = yf.download('^GSPC', start=start_date, end=end_date)['Close']
nasdaq = yf.download('^IXIC', start=start_date, end=end_date)['Close']
jones = yf.download('^DJI', start=start_date, end=end_date)['Close']
russell = yf.download('^RUT', start=start_date, end=end_date)['Close']
#Commodity
copper = yf.download('HG=F', start=start_date, end=end_date)['Close']
corn = yf.download('ZC=F', start=start_date, end=end_date)['Close']
soybean = yf.download('ZS=F', start=start_date, end=end_date)['Close']
wheat = yf.download('ZW=F', start=start_date, end=end_date)['Close']
gold = yf.download('GC=F', start=start_date, end=end_date)['Close']
silver = yf.download('SI=F', start=start_date, end=end_date)['Close']
oil = yf.download('CL=F', start=start_date, end=end_date)['Close']
#Forex
eur_usd = yf.download('EURUSD=X', start=start_date, end=end_date)['Close']
gbp_usd = yf.download('GBPUSD=X', start=start_date, end=end_date)['Close']
jpy_usd = yf.download('JPY=X', start=start_date, end=end_date)['Close']
aud_usd = yf.download('AUDUSD=X', start=start_date, end=end_date)['Close']
USD = yf.download('DX-Y.NYB', start=start_date, end=end_date)['Close']
#Treasury
bonds = yf.download('^TNX', start=start_date, end=end_date)['Close']
#Crypto
eth = yf.download('ETH-USD', start=start_date, end=end_date)['Close']
ltc = yf.download('LTC-USD', start=start_date, end=end_date)['Close']
xrp = yf.download('XRP-USD', start=start_date, end=end_date)['Close']
#Volatility
vix = yf.download('^VIX', start=start_date, end=end_date)['Close']
# Real Estate
reit = yf.download('VNQ', start=start_date, end=end_date)['Close']

data_dict = {
    'btc': btc,
    'sp500': sp500,
    'nasdaq': nasdaq,
    'jones': jones,
    'russell': russell,
    'copper': copper,
    'corn': corn,
    'soybean': soybean,
    'wheat': wheat,
    'gold': gold,
    'silver': silver,
    'oil': oil,
    'eur_usd': eur_usd,
    'gbp_usd': gbp_usd,
    'jpy_usd': jpy_usd,
    'aud_usd': aud_usd,
    'USD': USD,
    'bonds': bonds,
    'eth': eth,
    'ltc': ltc,
    'xrp': xrp,
    'vix': vix,
    'reit': reit
}

print(ddata_dict.keys())