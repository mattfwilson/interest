import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import yfinance as yf
import random
import pyautogui

stonks = ['AAPL', 'AMZN', 'MSFT']
graph_colors = ['forestgreen', 'red', 'royalblue', 'goldenrod', 'darkorange', 'darkviolet', 'olivedrab', 'dimgray']
ticker = 'AAPL'
start_date = '2010-01-01'
end_date = '2024-01-01'

def full_screen():
    pyautogui.hotkey('alt', 'space')
    pyautogui.hotkey('x')

#ticker = str(input('What stock would you like to parse? '))
#start_date = str(input(f'When should we start parsing for {ticker} (yyyy-mm-dd)? '))
#end_date = str(input(f'When should parsing end for {ticker} (yyyy-mm-dd)? '))
stock_data = yf.download(stonks, start=start_date, end=end_date)

plt.figure(figsize=(16, 10))
plt.plot(stock_data['Close'], label=stonks, color=random.choice(graph_colors))
full_screen()

#plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
plt.xlabel('Date', fontweight='bold', fontsize=16)
plt.ylabel('Stock Price', fontweight='bold', fontsize=16)
plt.title('Closing prices for {} from {} - {}'.format(stonks, start_date, end_date), fontweight='bold', fontsize=24, y=1.04)
plt.legend()

plt.show()

