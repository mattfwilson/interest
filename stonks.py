import matplotlib.pyplot as plt
import yfinance as yf
import random

graph_colors = ['forestgreen', 'red', 'royalblue', 'goldenrod', 'darkorange', 'darkviolet', 'olivedrab', 'dimgray']
ticker = 'AAPL'
start_date = '2010-01-01'
end_date = '2024-01-01'
rand_lst = [random.randint(1, 1000) for _ in range(1000)]

ticker = str(input('What stock would you like to parse? '))
start_date = str(input(f'When should we start parsing for {ticker} (yyyy-mm-dd)? '))
end_date = str(input(f'When should parsing end for {ticker} (yyyy-mm-dd)? '))
stock_data = yf.download(ticker, start=start_date, end=end_date)

plt.figure(figsize=(22, 12))
plt.plot(stock_data['Close'], label=ticker, color=random.choice(graph_colors))

plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Stock closing prices for {} from {} - {}'.format(ticker, start_date, end_date))
plt.legend()

plt.show()

