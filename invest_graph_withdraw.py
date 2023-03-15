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

principal = 675000
int_rate = .075
num_comp = 12
comp_years = 20
counter = 0
contribution = 22500
withdrawal = 75000
x_labels = []
y_labels = []
total_accrued = []

# compounding func appending each year to total list
def calc_investing(principal, rate, num_comp, time, contribution, counter):
    for year in range(time):
        principal += contribution
        amount = principal * (pow((1 + rate / num_comp), num_comp * (year + 1)))
        print(f'Year {year + 1} - ${round(amount, 2)}')
        counter += 1
        total_accrued.append(amount)
    return amount, counter

def calc_retirement(principal, rate, num_comp, withdraw, counter):
    while principal > 0:
        if principal > withdraw:
            counter += 1
            principal -= withdraw
            amount = principal * (pow((1 + rate / num_comp), num_comp * (counter + 1)))
            total_accrued.append(amount)
            print(f'Year {counter + 1} - ${round(amount, 2)}')
        else:
            principal -= principal
            counter += 1
    return principal, counter

# inputs
# principal = int(input('How much principal do you currently have saved? '))
# comp_years = int(input('How many more years do you plan to work? '))
# int_input = input('What is the current interest rate? (decimal) ')
# contribution = int(input('How much will you contribute per year? '))
# if int_input == '':
#     int_rate = float(hist_interest)
# else:
#     int_rate = float(int_input)

# count increment for graph tick labels
print(f'Counter before: {counter}')
invest_years, counter = calc_investing(principal, int_rate, num_comp, comp_years, contribution, counter)
retire_years, counter = calc_retirement(principal, int_rate, num_comp, withdrawal, counter)
print(f'Counter after: {counter}')

print(len(f'X labels: {x_labels}'))
print(len(f'Y labels: {y_labels}'))

y_labels.append(counter)
x_labels.append(counter)

print(f'Investment years: {invest_years}')
print(f'Retirement years: {retire_years}')
print(len(f'X labels: {x_labels}'))
print(len(f'Y labels: {y_labels}'))
print(f'Total Accrued: {total_accrued}')

percentage = '{:.2%}'.format(int_rate)
dollars = '{:,}'.format(invest_years)

# graph data with matplot
fig, ax = plt.subplots(figsize=(12, 9))
fig.suptitle(f'Compound principal + accrued interest over {comp_years} years', fontsize='20', fontweight='bold')
plt.title(f'Interest Rate: {percentage}, Total: ${dollars}', fontsize='12', fontweight='regular')

print(len(f'Length total accrued: {total_accrued}'))

plt.bar(range(counter-1), total_accrued, tick_label=range(counter-1), width=.5, color=['green'])
plt.ylabel('Total value', fontweight='bold')
ax.xaxis.set_label_coords(.5, -.07)
plt.xlabel('Years of compounding', fontweight='bold')
ax.yaxis.set_label_coords(-.1, .5)

plt.show()