import matplotlib.pyplot as plt
import yfinance as yf
import pyautogui

principal = 250000
int_rate = .07
withdraw_rate = 40000
inflation = .02
interest = 0
retire_years = 0

def calc_retire(principal, int_rate, withdraw_rate, retire_years):
    interest = principal * int_rate
    principal = principal - withdraw_rate
    total = principal + interest
    retire_years += 1
    return total, interest, retire_years

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

while principal > 0:
    res = calc_retire(principal, int_rate, withdraw_rate, retire_years)
    print(f'Year {res[2]} - Principal: ${round(res[0], 2)} (Interest: ${round(res[1], 2)})')
    principal = int(res[0])
    retire_years = int(res[2])
