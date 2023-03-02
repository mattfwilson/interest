import matplotlib
matplotlib.use('TkAgg', force=True)
from matplotlib import pyplot as plt

principal = 1000
int_rate = .06
percentage = "{:.2%}".format(int_rate)
num_comp = 12
growthYears = 15
yearCounter = 0
annual_contribution = 10000

left_label = []
bottom_label = []
accrued = []

def calc_compound(P, r, n, t):
    for year in range(t):
        amount = P * (pow((1 + r / n), n * (year + 1)))
        accrued.append(amount)
        print(f'Year {year + 1} - ${round(amount, 2)}')
    return amount

while yearCounter < growthYears:
    yearCounter += 1
    left_label.append(yearCounter)
    bottom_label.append(yearCounter)

principal = calc_compound(principal, int_rate, num_comp, growthYears)

print(f'Length of left label: {len(left_label)}')
print(f'Length of bottom label: {len(bottom_label)}')
print(f'Length of accrued: {len(accrued)}')

# graph with matplot
plt.title(f'Compound interest over {growthYears} years at {percentage} = ${round(principal, 2)}')
plt.bar(left_label, accrued, tick_label=bottom_label, width=.5, color=['green'])
plt.ylabel('Total value (by $Millions)')
plt.xlabel('Years of compounding')
plt.show()