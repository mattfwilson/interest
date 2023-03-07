import matplotlib.pyplot as plt
from matplotlib import pylab

# variables
principal = 50000
interest = .075
percentage = "{:.2%}".format(interest)
numCompounds = 1
yearCounter = 0
growthYears = 40
contribution = 70000
contribution_inc = .02
testInterest = []
left_label = []
bottom_label = []

# calculate compound interest
def calcInterest(principal, interest, numCompounds, contribution):
	accrued = (principal * (1 + (interest / numCompounds)) ** numCompounds) - principal
	principal = principal + accrued
	principal += contribution
	return principal, accrued

# calculate YOY totals
while yearCounter < growthYears:
    yearCounter += 1
    principal, interestDelta = calcInterest(principal, interest, numCompounds, contribution)
    principal = round(principal, 2)
    testInterest.append(principal)
    left_label.append(yearCounter)
    bottom_label.append(yearCounter)

# chart YOY totals
plt.title(f'Compound interest over {growthYears} years at {percentage} = ${principal}')
plt.bar(left_label, testInterest, tick_label = bottom_label, width = .75, color = ['green'])
plt.ylabel('Total value (by $Millions)')
plt.xlabel('Years of compounding')
plt.show()