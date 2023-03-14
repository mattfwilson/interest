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

principal = 0
int_rate = 0
num_comp = 12
comp_years = 0
counter = 0
contribution = 0
withdrawal = 75000
x_labels = []
y_labels = []
total_accrued = []
int_accrued = []

# compounding func appending each year to total list
def calc_compound(principal, rate, num_comp, time, contribution, counter):
    for year in range(time):
        principal += contribution
        amount = principal * (pow((1 + rate / num_comp), num_comp * (year + 1)))
        print(f'Year {year + 1} - ${round(amount, 2)}')
        counter += 1
        total_accrued.append(amount)
        y_labels.append(counter)
        x_labels.append(counter)
    return amount

def calc_withdraw(principal, rate, num_comp, withdraw, counter):
    while principal >= withdraw:
            counter += 1
            principal -= withdraw
            amount = principal * (pow((1 + rate / num_comp), num_comp * (counter + 1)))
            total_accrued.append(amount)
            print(f'Year {counter + 1} - ${round(amount, 2)}')
    principal -= principal
    counter += 1
    return principal

# inputs
principal = int(input('How much principal do you currently have saved? '))
comp_years = int(input('How many more years do you plan to work? '))
int_input = input('What is the current interest rate? (decimal) ')
contribution = int(input('How much will you contribute per year? '))
if int_input == '':
    int_rate = float(hist_interest)
else:
    int_rate = float(int_input)

# count increment for graph tick labels
invest_years = round(calc_compound(principal, int_rate, num_comp, comp_years, contribution, counter), 2)
retire_years = round(calc_withdraw(principal, int_rate, num_comp, withdrawal, counter), 2)

print(f'Investment years: {invest_years}')
print(f'Retirement years: {retire_years}')
print(len(f'X labels: {x_labels}'))
print(len(f'Y labels: {y_labels}'))

percentage = '{:.2%}'.format(int_rate)
dollars = '{:,}'.format(invest_years)

# graph data with matplot
fig, ax = plt.subplots(figsize=(12, 9))
fig.suptitle(f'Compound principal + accrued interest over {comp_years} years', fontsize='20', fontweight='bold')
plt.title(f'Interest Rate: {percentage}, Total: ${dollars}', fontsize='12', fontweight='regular')

plt.bar(x_labels, total_accrued, tick_label=y_labels, width=.5, color=['green'])
plt.ylabel('Total value', fontweight='bold')
ax.xaxis.set_label_coords(.5, -.07)
plt.xlabel('Years of compounding', fontweight='bold')
ax.yaxis.set_label_coords(-.1, .5)

plt.show()