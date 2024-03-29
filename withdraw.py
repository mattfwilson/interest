import matplotlib.pyplot as plt
import yfinance as yf
import pyautogui

age = 37
principal = 750000
int_rate = .06
withdraw_rate = 45000
inflation = .02
num_comp = 1
years = []
net_worth = []

def calc_retire(principal, int_rate, withdraw_rate, age, num_comp):
    old_principal = principal
    interest = 0
    principal = principal * pow(((1 + int_rate / num_comp)), (num_comp * 1))
    interest = principal - old_principal
    principal = principal - withdraw_rate
    age += 1
    years.append(age)
    net_worth.append(principal)
    return principal, age, interest

def full_screen():
    pyautogui.hotkey('alt', 'space')
    pyautogui.hotkey('x')

def show_graph():
    colors = ['red' if value < 0 else 'green' for value in net_worth]
    plt.bar(years, net_worth, color=colors)
    plt.xlabel('Retirement Years', fontweight='bold', fontsize=16)
    plt.ylabel('Net Worth', fontweight='bold', fontsize=16)
    plt.title(f'Withdrawing ${withdraw_rate:,} annually, growing at {int_rate}% with {inflation}% inflation', fontsize=26, fontweight='bold', y=1.04)
    plt.legend()

    full_screen()
    plt.show()

if __name__ == '__main__':
    while principal > 0:
        res = calc_retire(principal, int_rate, withdraw_rate, age, num_comp)
        print(f'Year {res[1]} - Principal: ${round(res[0], 2):,} (Interest: ${round(res[2], 2):,}/year - ${round(res[2] / 12, 2)}/month)')
        principal = res[0]
        age = res[1]
        if age > 99:
            break

show_graph()
