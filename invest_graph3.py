import matplotlib
matplotlib.use('TkAgg', force=True)
from matplotlib import pyplot as plt

principal = 50000
int_rate = .07
percentage = "{:.2%}".format(int_rate)
num_comp = 12
comp_years = 25
counter = 0
contribution = 10000
left_label = []
bottom_label = []
accrued = []

# compounding func appending each year to accrued list
def calc_compound(P, r, n, t):
    for year in range(t):
        amount = P * (pow((1 + r / n), n * (year + 1)))
        accrued.append(amount)
        print(f'Year {year + 1} - ${round(amount, 2)}')
    return amount

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
plt.title(f'Compound interest over {comp_years} years at {percentage} = ${dollars}', fontsize='20', fontweight='bold')
plt.bar(left_label, accrued, tick_label=bottom_label, width=.5, color=['green'])
plt.ylabel('Total value (by $Millions)')
plt.xlabel('Years of compounding')
plt.show()