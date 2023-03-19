##### TO-DOS ################################################################################################

# Add function that calculates interest only
# Create stacked bar graphs showing individual principal vs interest growth
# Make y ticks more consumable
# Create formula to show how saving x amount more years equates to y amount more years in retirement

from matplotlib import pyplot as plt
import datetime
from returns import *

age = 36
principal = 650000
int_rate = .075
num_comp = 12
comp_years = 12
contribution = 40000
withdrawal = 58253 # Massachusetts average
year_totals = []
year_labels = []
interest = []
counter = 0

##### Compounding + withdrawal + peak total functions #########################################################

def calc_invest(principal, rate, num_comp, time, contribution, year_count):
    for year in range(time):
        principal += contribution
        amount = principal * (pow((1 + rate / num_comp), num_comp * (year + 1)))
        year_totals.append(amount)
        print(f'Year {year + 1} - ${round(amount, 2)}')
        year_count += 1
    return amount, year_count

def calc_retire(principal, rate, num_comp, withdraw, year_count):
    while principal > 0:
        principal -= withdraw
        year_totals.append(principal)
        print(f'Year {year_count + 1} - ${round(principal, 2)}')
        year_count += 1
        if principal < withdraw:
            principal -= principal
    return principal, year_count

def calc_peak_total(years):
    today = datetime.date.today()  
    current_year = today.year

    for year in year_totals:
        year_labels.append(current_year)
        current_year += 1  
    for total in years:
        if total == max(years):
            peak_total = total
            max_index = years.index(peak_total)
    return max_index

##### User input ###############################################################################################

# principal = int(input('How much money do you currently have saved? '))
int_principal = principal
# comp_years = int(input('How many more years do you plan to work? '))
# int_input = input('What is the your presumed interest rate? ')
# if int_input == '':
#     int_rate = float(hist_interest)
#     print(f'Using average return of 10 year S&P 500 of {hist_interest}')
# else:
#     int_rate = float(int_input) *.01
# contribution = int(input('How much money will you contribute/save per year? '))
# withdrawal = int(input('How much do you want your retirement salary to be? '))

##### Call functions and format results #########################################################################

principal, counter = calc_invest(principal, int_rate, num_comp, comp_years, contribution, counter)
retire_years, counter = calc_retire(principal, int_rate, num_comp, withdrawal, counter)
max_year = calc_peak_total(year_totals)

percentage = '{:.2%}'.format(int_rate)
round_dollars = round(principal, 2)
subtitle_dollars = '{:,}'.format(round_dollars)
title_dollars = '{:,}'.format(int_principal)
print(interest)

##### Graph data ################################################################################################

fig, ax = plt.subplots(figsize=(15, 9))
fig.suptitle(f'Compound growth of ${title_dollars} over {comp_years} years', fontsize='20', fontweight='bold')
plt.title(f'At {percentage} interest, you will retire in {year_labels[max_year]} with a peak savings of ${subtitle_dollars}. You will be {age + len(year_totals)} when your savings runs out in {year_labels[-1]}', fontsize='11', fontweight='regular', y=1.03)

colors = ['indianred' if year_totals.index(x) > max_year else 'olivedrab' for x in year_totals]
plt.bar(range(counter), year_totals, tick_label=year_labels, width=.5, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Total value (millions)', fontweight='bold')
ax.xaxis.set_label_coords(.5, -.1)
plt.xlabel('Years of compounding/withdrawing', fontweight='bold')
ax.yaxis.set_label_coords(-.05, .5)

plt.show()