import matplotlib.pyplot as plt
from matplotlib import pylab

# variables
principal = 650000
int_rate = .05
percentage = "{:.2%}".format(int_rate)
num_comp = 12
yearCounter = 0
growthYears = 15
contribution = 40000
contribution_inc = .02
testInterest = []
left_label = []
bottom_label = []

# calculate compound int_rate
def calc_compound(principal, int_rate, num_comp, years, contribution):
	amount = principal * (pow((1 + int_rate / num_comp), num_comp * (years + 1)))
	principal = principal + amount
	principal += contribution
	return principal, amount

# calculate YOY totals
while yearCounter < growthYears:
    yearCounter += 1
    principal, interestDelta = calc_compound(principal, int_rate, num_comp, growthYears, contribution)
    principal = round(principal, 2)
    testInterest.append(principal)
    left_label.append(yearCounter)
    bottom_label.append(yearCounter)

# chart YOY totals
plt.title(f'Compound int_rate over {growthYears} years at {percentage} = ${principal}')
plt.bar(left_label, testInterest, tick_label = bottom_label, width = .75, color = ['green'])
plt.ylabel('Total value (by $Millions)')
plt.xlabel('Years of compounding')
plt.show()