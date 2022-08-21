import matplotlib.pyplot as plt
from matplotlib import pylab

# variables to play with
principal = 50000
interest = .075
percentage = "{:.2%}".format(interest)
numCompounds = 1
yearCounter = 0
growthYears = 20
contribution = 36000
testDollars = []
testInterest = []
interestDelta = []
left = [] # x-coordinates of left sides of bars
tick_label = [] # labels for bars

# calculate compound interest
def calcInterest(principal, interest, numCompounds, contribution):
	accrued = (principal * (1 + (interest / numCompounds)) ** numCompounds) - principal
	principal = principal + accrued
	principal += contribution
	return principal, accrued

# show YOY summary
while yearCounter < growthYears:
    yearCounter += 1
    principal, interestDelta = calcInterest(principal, interest, numCompounds, contribution)
    principal = round(principal, 2)
    interestDelta = round(interestDelta, 2)
    testInterest.append(principal)
    left.append(yearCounter)
    tick_label.append(yearCounter)

# show chart
plt.title(f'Compound interest over {growthYears} years at {percentage}')
plt.bar(left, testInterest, tick_label = tick_label, width = .75, color = ['green']) # plotting a bar chart
plt.ylabel('Total value (by $Millions)') # naming the y-axis
plt.xlabel('Years of compounding')# naming the x-axis
plt.show() # function to show the plot chart