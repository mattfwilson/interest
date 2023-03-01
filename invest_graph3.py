import matplotlib.pyplot as plt

principal = 250000
int_rate = .05
percentage = "{:.2%}".format(int_rate)
num_comp = 12
growthYears = 15
annual_contribution = 10000

testInterest = []
left_label = []
bottom_label = []

def calc_compound(p, r, n, t):
    for period in range(t):
        acrrued = p * (pow((1 + r / n), n * (period + 1)))
        print(f'Year {period + 1} - ${round(acrrued, 2)}')
    return acrrued

principal = calc_compound(principal, int_rate, num_comp, growthYears)
principal = round(principal, 2)
testInterest.append(principal)
left_label.append(principal)
bottom_label.append(range(growthYears))

# graph with matplot
plt.title(f'Compound int_rate over {growthYears} years at {percentage} = ${principal}')
plt.bar(left_label, testInterest, tick_label=bottom_label, width=.75, color=['green'])
plt.ylabel('Total value (by $Millions)')
plt.xlabel('Years of compounding')
plt.show()