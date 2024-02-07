import matplotlib.pyplot as plt
import yfinance as yf

ticker_symbol = '^GSPC'
stock_data = yf.download(ticker_symbol, start='1950-01-01', end='1985-01-01')

plt.figure(figsize=(22, 12))
plt.plot(stock_data['Close'], label='Close', color='blue')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price of {}'.format(ticker_symbol))
plt.legend()

plt.show()

