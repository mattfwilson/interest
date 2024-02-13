import matplotlib.pyplot as plt
import yfinance as yf
import pyautogui

principal = 250000
int_rate = .07
withdraw_rate = .04
inflation = .02


def full_screen():
    pyautogui.hotkey('alt', 'space')
    pyautogui.hotkey('x')

def show_graph():
    plt.plot(principal, label=stock, color=selected_color)
    plt.xlabel('Date', fontweight='bold', fontsize=16)
    plt.ylabel('Stock Price', fontweight='bold', fontsize=16)
    plt.title('Withdrawing {}% of ${} growing at {}% with {}% inflation'.format(withdraw_rate, principal, interest, inflation, fontweight='bold', fontsize=24, y=1.04))
    plt.legend()

    full_screen()
    plt.show()

show_graph()
