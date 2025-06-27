import matplotlib.pyplot as plt

age = 37
principal = 1150000
int_rate = .07
int_accrued = 0
withdraw_rate = 50000
inflation = .02
num_comp = 1
ss_contribution = 2000
retire_years = []
net_worth = []

def calc_retire(principal, age, int_accrued, ss, withdraw):
    if age > 61:
        principal += ss

    old_principal = principal
    new_principal = principal * (pow((1 + int_rate / 100), 12))
    int_accrued = new_principal - old_principal
    new_principal -= withdraw

    age += 1
    retire_years.append(age)
    net_worth.append(new_principal)

    return new_principal, age, int_accrued, ss, withdraw

def show_graph():
    colors = ['red' if value < 0 else 'green' for value in net_worth]
    plt.figure(figsize=(20, 12))
    plt.bar(retire_years, net_worth, color=colors)
    plt.xlabel('Retirement retire_years', fontweight='bold', fontsize=16)
    plt.ylabel('Net Worth', fontweight='bold', fontsize=16)
    plt.title(f'Withdrawing ${withdraw_rate}, annually, growing at {int_rate}% with {inflation}% inflation', fontsize=26, fontweight='bold', y=1.04)
    plt.legend()
    plt.show()

while age < 100:
    if principal > 2500000:
        break
    else:
        principal, age, int_accrued, ss_contribution, withdraw_rate = calc_retire(principal, age, int_accrued, ss_contribution, withdraw_rate)
        print(f'Age: {age} - Principal: {principal}')

show_graph()
