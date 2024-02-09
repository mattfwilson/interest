import matplotlib.pyplot as plt
import yfinance as yf
import random
import pyautogui

stock_lst = ['AAPL', 'AMZN', 'MSFT', 'NVDA', 'TSLA']
colors = ['forestgreen', 'red', 'royalblue', 'goldenrod', 'darkorange', 'darkviolet', 'olivedrab', 'dimgray', 'lightblue', 'orange']
ticker = 'AAPL'
start_date = '2010-01-01'
end_date = '2024-01-01'
stock_data = yf.download(stock_lst, start=start_date, end=end_date)

def full_screen():
    pyautogui.hotkey('alt', 'space')
    pyautogui.hotkey('x')

def individualize(stocks):
    for stock in stocks:
        selected_color = random.choice(colors)
        colors.remove(selected_color)
        stock_data = yf.download(stock, start=start_date, end=end_date)
        plt.plot(stock_data['Close'], label=stock, color=selected_color)

individualize(stock_lst)

plt.xlabel('Date', fontweight='bold', fontsize=16)
plt.ylabel('Stock Price', fontweight='bold', fontsize=16)
plt.title('Closing prices for {} from {} - {}'.format(stock_lst, start_date, end_date), fontweight='bold', fontsize=24, y=1.04)
plt.legend()

full_screen()
plt.show()

