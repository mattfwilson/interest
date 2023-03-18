##### TO-DOS ################################################################################################

# Add function that calculates interest only
# Create stacked bar graphs showing individual principal vs interest growth
# Make y ticks more consumable

from matplotlib import pyplot as plt
import datetime

age = 30
principal = 20000
int_principal = principal
int_rate = .075
num_comp = 12
comp_years = 25
contribution = 16500
withdrawal = 70000
year_totals = []
year_labels = []
interest = []
counter = 0

##### Compounding + withdrawal + peak total functions #########################################################

def calc_invest(principal, rate, num_comp, time, contribution, year_count):
    for year in range(time):
        principal += contribution
        amount = principal * (pow((1 + rate / num_comp), num_comp * (year + 1)))
        comp_int = amount - principal
        interest.append(comp_int)
        year_totals.append(amount)
        print(f'Year {year + 1} - ${round(amount, 2)}')
        year_count += 1
    return amount, year_count

def calc_retire(principal, rate, num_comp, withdraw, year_count):
    while principal > 0:
        if principal > withdraw:
            principal -= withdraw
            year_totals.append(principal)
            print(f'Year {year_count + 1} - ${round(principal, 2)}')
            year_count += 1
        else:
            principal -= principal
    return principal, year_count

def calc_peak_total(years):
    today = datetime.date.today()  
    current_year = today.year

    for i in year_totals:
        year_labels.append(current_year)
        current_year += 1  
    for total in years:
        if total == max(years):
            peak_total = total
            max_index = years.index(peak_total)
    return max_index

##### Call functions and format results #######################################################################

principal, counter = calc_invest(principal, int_rate, num_comp, comp_years, contribution, counter)
retire_years, counter = calc_retire(principal, int_rate, num_comp, withdrawal, counter)
max_year = calc_peak_total(year_totals)

percentage = '{:.2%}'.format(int_rate)
round_dollars = round(principal, 2)
comma_dollars = '{:,}'.format(round_dollars)
print(interest)

##### Graph data ##############################################################################################

fig, ax = plt.subplots(figsize=(14, 9))
fig.suptitle(f'Compound growth over of ${int_principal} over {comp_years} years', fontsize='20', fontweight='bold')
plt.title(f'Interest: {percentage} -- Year {year_labels[max_year]} peak savings: ${comma_dollars} -- {age + len(year_totals)} years old when savings runs out in {year_labels[-1]}', fontsize='12', fontweight='regular')

colors = ['indianred' if year_totals.index(x) > max_year else 'olivedrab' for x in year_totals]
plt.bar(range(counter), year_totals, tick_label=year_labels, width=.5, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Total value (millions)', fontweight='bold')
ax.xaxis.set_label_coords(.5, -.1)
plt.xlabel('Years of compounding/withdrawing', fontweight='bold')
ax.yaxis.set_label_coords(-.05, .5)

plt.show()