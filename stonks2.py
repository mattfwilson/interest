import matplotlib.pyplot as plt
import yfinance as yf
import random
import pyautogui

stock_lst = ['AAPL', 'AMZN', 'MSFT', 'NVDA', 'TSLA']
colors = ['red', 'royalblue', 'goldenrod', 'darkorange', 'darkviolet', 'olivedrab', 'dimgray']
ticker = 'AAPL'
start_date = '2010-01-01'
end_date = '2024-01-01'
stock_data = yf.download(stock_lst, start=start_date, end=end_date)

def full_screen():
    pyautogui.hotkey('alt', 'space')
    pyautogui.hotkey('x')

def clean_date(date):
    months = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    clean_month = months[date[-5:-3]]
    clean_day = ''
    if date[-2] == '0':
        clean_day = date[-1]
    else:
        clean_day = date[-2:]
    clean_year = date[:4]
    clean_date = clean_month + ' ' + clean_day + ', ' + clean_year
    return clean_date

def parse_stocks(stocks):
    for stock in stocks:
        selected_color = random.choice(colors)
        colors.remove(selected_color)
        stock_data = yf.download(stock, start=start_date, end=end_date)
        plt.plot(stock_data['Close'], label=stock, color=selected_color)

def show_graph():
    plt.xlabel('Date', fontweight='bold', fontsize=16)
    plt.ylabel('Stock Price', fontweight='bold', fontsize=16)
    plt.title('Closing prices for {} from {} - {}'.format(stock_lst, clean_date(start_date), clean_date(end_date)), fontweight='bold', fontsize=24, y=1.04)
    plt.legend()

    full_screen()
    plt.show()

parse_stocks(stock_lst)
show_graph()
