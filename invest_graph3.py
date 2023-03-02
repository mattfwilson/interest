import matplotlib
matplotlib.use('TkAgg',force=True)
from matplotlib import pyplot as plt

principal = 1000
int_rate = .06
percentage = "{:.2%}".format(int_rate)
num_comp = 12
growthYears = 5
annual_contribution = 10000

left_label = []
bottom_label = []

def calc_compound(P, r, n, t):
    for year in range(t):
        acrrued = P * (pow((1 + r / n), n * (year + 1)))
        print(f'Year {year + 1} - ${round(acrrued, 2)}')
    return acrrued

principal = calc_compound(principal, int_rate, num_comp, growthYears)
left_label.append(principal)
bottom_label.append(range(growthYears))

print(f'Length of left label: {len(left_label)}')
print(f'Length of bottom label: {len(bottom_label)}')

# graph with matplot
# plt.title(f'Compound int_rate over {growthYears} years at {percentage} = ${principal}')
# plt.bar(left_label, principal, tick_label=bottom_label, width=.75, color=['green'])
# plt.ylabel('Total value (by $Millions)')
# plt.xlabel('Years of compounding')
# plt.show()