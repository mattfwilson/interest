import matplotlib
matplotlib.use('TkAgg', force=True)
from matplotlib import pyplot as plt
from matplotlib import pylab

principal = 700000
int_rate = .09
num_comp = 12
comp_years = 13
counter = 0
contribution = 10000
left_label = []
bottom_label = []
total = []
int_accrued = []

# compounding func appending each year to total list
def calc_compound(P, r, n, t):
    for year in range(t):
        amount = P * (pow((1 + r / n), n * (year + 1)))
        total.append(amount)
        print(f'Year {year + 1} - ${round(amount, 2)}')
    return amount

# input
# principal = int(input('How much do you currently have saved? '))
# comp_years = int(input('How many years until retirement? '))
# int_rate = float(input('What is the current interest rate? '))
percentage = '{:.2%}'.format(int_rate)

# count increment for graph tick labels
while counter < comp_years:
    counter += 1
    left_label.append(counter)
    bottom_label.append(counter)

# instantiate calc_compound
compounded = round(calc_compound(principal, int_rate, num_comp, comp_years), 2)
dollars = '{:,}'.format(compounded)

# graph data with matplot
fig, ax = plt.subplots(figsize=(12, 9))
fig.suptitle(f'Compound principal + accrued interest over {comp_years} years', fontsize='20', fontweight='bold')
plt.title(f'Interest Rate: {percentage}, Total: ${dollars}', fontsize='12', fontweight='regular')
plt.bar(left_label, total, tick_label=bottom_label, width=.5, color=['green'])
plt.ylabel('Total value', fontweight='bold')
ax.xaxis.set_label_coords(.5, -.07)
plt.xlabel('Years of compounding', fontweight='bold')
ax.yaxis.set_label_coords(-.1, .5)
plt.show()