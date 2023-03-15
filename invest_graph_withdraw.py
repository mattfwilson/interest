##### TO-DOS #####
# Add in birthdate to calculate time to required retirement withdrawal
# Add function that calculates interest only
# Create stacked bar graphs showing individual principal vs interest growth
# Create function to calculate a withdrawal amount until principal hits zero

import matplotlib
matplotlib.use('TkAgg', force=True)
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from returns import *

principal = 650000
int_rate = .075
num_comp = 12
comp_years = 15
counter = 0
contribution = 22500
withdrawal = 75000
x_labels = []
y_labels = []
year_total = []

# compounding func appending each year to total list
def calc_investing(principal, rate, num_comp, time, contribution, counter):
    for year in range(time):
        principal += contribution
        amount = principal * (pow((1 + rate / num_comp), num_comp * (year + 1)))
        year_total.append(amount)
        print(f'Year {year + 1} - ${round(amount, 2)}')
        counter += 1
    return amount, counter

def calc_retirement(principal, rate, num_comp, withdraw, counter):
    while principal > 0:
        if principal > withdraw:
            principal -= withdraw
            year_total.append(principal)
            print(f'Year {counter + 1} - ${round(principal, 2)}')
            counter += 1
        else:
            principal -= principal
    return principal, counter

# count increment for graph tick labels
principal, counter = calc_investing(principal, int_rate, num_comp, comp_years, contribution, counter)
retire_years, counter = calc_retirement(principal, int_rate, num_comp, withdrawal, counter)

print(f'Investment years: {principal}')
print(f'Retirement years: {retire_years}')
print(len(f'X labels: {x_labels}'))
print(len(f'Y labels: {y_labels}'))
print(f'Total Accrued: {year_total}')

percentage = '{:.2%}'.format(int_rate)
round_dollars = round(principal, 2)
comma_dollars = '{:,}'.format(round_dollars)

# graph data with matplot
fig, ax = plt.subplots(figsize=(14, 9))
fig.suptitle(f'Compound principal + accrued interest over {comp_years} years', fontsize='20', fontweight='bold')
plt.title(f'Interest Rate: {percentage} -- Retirement year total: ${comma_dollars}', fontsize='12', fontweight='regular')

colors = ['yellowgreen' if i < max(year_total) else 'olivedrab' for i in year_total]
plt.bar(range(counter), year_total, tick_label=range(counter), width=.5, color=colors)
plt.ylabel('Total value (millions)', fontweight='bold')
ax.xaxis.set_label_coords(.5, -.07)
plt.xlabel('Years of compounding/withdrawing', fontweight='bold')
ax.yaxis.set_label_coords(-.1, .5)

plt.show()